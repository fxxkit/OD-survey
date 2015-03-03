# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, make_response, Response, jsonify, request, send_from_directory
import settings
import json
import datetime
import pymongo
import logging

## init logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

## create a connection to MongoLab
logging.info('connect to %s' % settings.MONGODB_URI)
con = pymongo.MongoClient(settings.MONGODB_URI)
db = con.get_default_database()
logging.info('use database "%s"' % db.name)
co = db['survery']
logging.info('use collection "%s"' % co.full_name)

@app.route('/')
def show_index():
    return render_template( 'index.tpl', settings=settings )

@app.route('/digest', methods=['GET', 'POST'])
def digest():
    if request.method == 'GET':
        pass
    else:
        # receive POST request
        data = json.loads(request.data)
        logging.info('receive user response with length: %d' % len(request.data))

        # collect metadata
        data['ip'] = request.remote_addr
        data['time'] = datetime.datetime(data['time']['year'], data['time']['month'], data['time']['date'], data['time']['hour'], data['time']['minute'])

        # insert to collection
        mid = co.insert(data)

        if mid:
            resp = jsonify({'status': 'ok'})
            resp.status_code = 200
            logging.info('insert collectly')
        else:
            resp = jsonify({'status': 'mongo failed'})
            resp.status_code = 500
            logging.warning('insert failed')
        return resp

if __name__ == "__main__":

    import getopt, sys

    port = 5000
    app.debug = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],'p:d',['port=', 'debug'])
    except getopt.GetoptError:
        exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--port'): port = int(arg.strip())
        elif opt in ('-d','--debug'): app.debug = True

    app.run(host='0.0.0.0', port=port)






