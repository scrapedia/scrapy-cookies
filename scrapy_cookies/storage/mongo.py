import logging
import pickle
import re
from itertools import starmap

import pymongo
from pymongo import MongoClient
from scrapy.http.cookies import CookieJar

from scrapy_cookies.storage import BaseStorage
from six.moves.http_cookiejar import Cookie

logger = logging.getLogger(__name__)
pattern = re.compile('^COOKIES_MONGO_MONGOCLIENT_(?P<kwargs>(?!KWARGS).*)$')


def get_arguments(var):
    return {str: {'name': var}, dict: var}[type(var)]


def write_cookiejar(cookiejar):
    return pickle.dumps(cookiejar)


def read_cookiejar(document):
    try:
        return pickle.loads(document['cookiejar'])
    except TypeError:
        return None


def convert_cookiejar(cookiejar):
    def _convert_cookies(x):
        if isinstance(x, (str, int, bool)):
            return x
        elif isinstance(x, Cookie):
            return dict(map(
                lambda attr: (attr, getattr(x, attr)),
                ("version", "name", "value", "port", "port_specified", "domain",
                 "domain_specified", "domain_initial_dot", "path",
                 "path_specified", "secure", "expires", "discard", "comment",
                 "comment_url")
            ))

        elif isinstance(x, dict):
            return dict(starmap(
                lambda k, v: (_convert_cookies(k), _convert_cookies(v)),
                x.items()
            ))

    return _convert_cookies(cookiejar._cookies)


class MongoStorage(BaseStorage):
    def __init__(self, settings):
        super(MongoStorage, self).__init__(settings)
        self.mongo_settings = dict(starmap(
            lambda k, v: (pattern.sub(lambda x: x.group(1).lower(), k), v),
            filter(lambda pair: pattern.match(pair[0]),
                   settings.copy_to_dict().items())
        ))
        self.mongo_settings.update(
            self.settings['COOKIES_MONGO_MONGOCLIENT_KWARGS']
        )
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
        self.coll.update_one(
            {'key': k},
            {'$set': {'key': k, 'cookiejar': write_cookiejar(v),
                      'cookies': convert_cookiejar(v)}},
            upsert=True
        )
