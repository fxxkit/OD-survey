# -*- coding: utf-8 -*-
import settings
import sys
from connect_mongolab import MongoLab

filename = 'survery.pkl'

if __name__ == '__main__':

    print 'connecting ...', 
    sys.stdout.flush()
    
    mongo = MongoLab(mongolab_uri=settings.MONGODB_URI)

    print '[ok]'

    print 'fetching ...', 
    sys.stdout.flush()

    mongo.fetch_all()

    current = mongo.load(fn=filename)

    print '[ok] (%d data fetched, was %d)' % (len(mongo.data), len(current))

    if len(current) < len(mongo.data):
        print 'update', filename
        mongo.save(dump_fn=filename, overwrite=True)
    else:
        print 'no updates.'

    mongo.bye()
