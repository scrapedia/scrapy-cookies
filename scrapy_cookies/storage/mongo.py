import logging
import pickle
import pymongo
import re
from itertools import starmap

from pymongo import MongoClient
from scrapy.http.cookies import CookieJar

from scrapy_cookies.storage import BaseStorage

logger = logging.getLogger(__name__)
pattern = re.compile('^COOKIES_MONGO_MONGOCLIENT_')


def get_arguments(var):
    return {str: {'name': var}, dict: var}[type(var)]


def write_cookiejar(cookiejar):
    return pickle.dumps(cookiejar)


def read_cookiejar(document):
    try:
        return pickle.loads(document['cookiejar'])
    except TypeError:
        return None


class MongoStorage(BaseStorage):
    def __init__(self, settings):
        super(MongoStorage, self).__init__(settings)
        self.mongo_settings = dict(starmap(
            lambda k, v: (
                k.replace('COOKIES_MONGO_MONGOCLIENT_', '').lower(), v),
            filter(lambda pair: pattern.match(pair[0]),
                   settings.copy_to_dict().items())
        ))
        self.mongo_settings.update(self.mongo_settings.pop('kwargs'))
        self.client = None
        self.db = None
        self.coll = None

    @classmethod
    def from_middleware(cls, middleware):
        return cls(middleware.settings)

    def open_spider(self, spider):
        self.client = MongoClient(**self.mongo_settings)

        self.db = self.client.get_database(
            **get_arguments(self.settings['COOKIES_MONGO_DATABASE'])
        )
        self.coll = self.db.get_collection(
            **get_arguments(self.settings['COOKIES_MONGO_COLLECTION'])
        )
        self.coll.create_index([('key', pymongo.ASCENDING)], unique=True)

    def close_spider(self, spider):
        self.client.close()

    def __missing__(self, k):
        cookiejar = CookieJar()
        self[k] = cookiejar
        return cookiejar

    def __delitem__(self, v):
        self.coll.delete_one({})

    def __getitem__(self, k):
        v = read_cookiejar(self.coll.find_one({'key': k}))
        if isinstance(v, CookieJar):
            return v
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, k)
        raise KeyError(k)

    def __iter__(self):
        return iter(self.coll.find())

    def __len__(self):
        return self.coll.count_documents({})

    def __setitem__(self, k, v):
        self.coll.insert_one({
            'key': k, 'cookiejar': write_cookiejar(v), 'cookies': v._cookies
        })
