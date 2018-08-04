import pickle
from collections import Iterable
from unittest import TestCase

import ujson
from scrapy import Spider
from scrapy.http.cookies import CookieJar
from scrapy.settings import Settings

from scrapy_cookies.settings import default_settings
from scrapy_cookies.storage.redis_ import RedisStorage


class RedisStorageTest(TestCase):
    maxDiff = None
    local_settings = {}

    def setUp(self):
        self.spider = Spider('foo')
        self.settings = Settings()
        self.settings.setmodule(default_settings)
        self.settings.setdict(self.local_settings)
        self.storage = RedisStorage(self.settings)
        self.storage.open_spider(self.spider)

    def tearDown(self):
        self.storage.close_spider(self.spider)
        self.storage.r.flushall()

    def test_getitem(self):
        cookies = CookieJar()
        self.storage.r.hmset(
            'new_cookies',
            {'cookiejar': pickle.dumps(cookies),
             'cookies': ujson.dumps(cookies._cookies)}
        )

        self.assertDictEqual(self.storage['new_cookies']._cookies,
                             cookies._cookies)

    def test_missing(self):
        self.assertDictEqual(self.storage['no_exist_cookies']._cookies,
                             CookieJar()._cookies)

    def test_setitem(self):
        cookies = CookieJar()
        self.storage['new_cookies'] = cookies
        self.assertDictEqual(
            pickle.loads(
                self.storage.r.hgetall('new_cookies')['cookiejar']
            )._cookies,
            cookies._cookies
        )
        self.assertDictEqual(
            self.storage.r.hgetall('new_cookies'),
            {'cookiejar': pickle.dumps(cookies),
             'cookies': ujson.dumps(cookies._cookies)}
        )

    def test_iter(self):
        self.assertIsInstance(self.storage, Iterable)

    def test_len(self):
        self.assertEqual(len(self.storage), 0)
        self.storage['new_cookies_1'] = CookieJar()
        self.assertEqual(len(self.storage), 1)
        self.storage['new_cookies_2'] = CookieJar()
        self.assertEqual(len(self.storage), 2)

    def test_delitem(self):
        self.storage['new_cookies'] = CookieJar()
        del self.storage['new_cookies']
        self.assertFalse(self.storage.r.hgetall('new_cookies'))
