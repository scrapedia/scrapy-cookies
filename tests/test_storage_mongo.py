import pickle
from collections import Iterable
from unittest import TestCase

from scrapy import Spider
from scrapy.http.cookies import CookieJar
from scrapy.settings import Settings

from scrapy_cookies.settings import default_settings
from scrapy_cookies.storage.mongo import MongoStorage


class MongoStorageTest(TestCase):
    local_settings = {
        'COOKIES_STORAGE': 'scrapy_cookies.storage.mongo.MongoStorage',
        'COOKIES_MONGO_MONGOCLIENT_HOST': 'localhost',
        'COOKIES_MONGO_MONGOCLIENT_PORT': 27017,
        'COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS': dict,
        'COOKIES_MONGO_MONGOCLIENT_TZ_AWARE': False,
        'COOKIES_MONGO_MONGOCLIENT_CONNECT': True,
        'COOKIES_MONGO_MONGOCLIENT_KWARGS': {},
        'COOKIES_MONGO_DATABASE': 'cookies',
        'COOKIES_MONGO_COLLECTION': 'cookies',
    }

    def setUp(self):
        self.spider = Spider('foo')
        self.settings = Settings()
        self.settings.setmodule(default_settings)
        self.settings.setdict(self.local_settings)
        self.storage = MongoStorage(self.settings)
        self.storage.open_spider(self.spider)

    def tearDown(self):
        self.storage.close_spider(self.spider)
        self.storage.coll.delete_many({})

    def test_getitem(self):
        cookies = CookieJar()
        self.storage.coll.insert_one({
            'key': 'new_cookies', 'cookiejar': pickle.dumps(cookies),
            'cookies': cookies._cookies
        })

        self.assertDictEqual(self.storage['new_cookies']._cookies,
                             cookies._cookies)

    def test_missing(self):
        self.assertDictEqual(self.storage['no_exist_cookies']._cookies,
                             CookieJar()._cookies)

    def test_setitem(self):
        cookies = CookieJar()
        self.storage['new_cookies'] = cookies
        self.assertDictEqual(
            self.storage.coll.find_one({'key': 'new_cookies'}, {'_id': 0}),
            {'key': 'new_cookies', 'cookiejar': pickle.dumps(cookies),
             'cookies': cookies._cookies}
        )

    def test_iter(self):
        self.assertIsInstance(self.storage, Iterable)
