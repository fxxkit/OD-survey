# -*- coding: utf-8 -*-
import pymongo
import settings

SEED_DATA = [
    {
        # metadata
        'ip': '10.90.255.254',
        'gender': 'other',
        'age': '3',
        'time': '2015-03-03 22:09:00',

        # opinions
        'opinions': [
            {
                'opid': 'notbad',
                'score': '3',
                'text': u'不錯'
            },
            {
                'opid': 'awesome',
                'score': '5',
                'text': u'讚啦'
            }            
        ],
        # scenarios
        'scenarios': [
            'brunch',
            'steak',
            'XDD'
        ]
    }
]

class MongoLab(object):
    """
    """
    def __init__(self, mongolab_uri, db='__default__', collection='survery'):
        self.con = pymongo.MongoClient(mongolab_uri)
        if db == '__default__':
            self.db = self.con.get_default_database()
        else:
            self.db = self.con[db]

        self.co = self.db[collection]

    def insert(self, data):
        mdocid = self.co.insert(data)
        return mdocid

    def fetch_all(self):
        return list(self.co.find())
        
    def bye(self):
        self.con.close()

if __name__ == '__main__':

    mongo = MongoLab(mongolab_uri=settings.MONGODB_URI, collection='test')

    mongo.insert(SEED_DATA)

    print mongo.fetch_all()

    mongo.bye()