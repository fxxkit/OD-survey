# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, make_response, Response, jsonify, request
import settings

app = Flask(__name__)


###############################
##         Locations         ##
###############################

@app.route('/')
def show_index():
    scenarios = [u'café', u'熱炒', u'居酒屋', u'拉麵', u'酒吧', u'下午茶', u'早餐店']
    return render_template( 'index.tpl', title=settings.SITE_TITLE, scenarios=scenarios )

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






