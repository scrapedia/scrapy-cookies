import os
import tempfile
from copy import deepcopy
from unittest import TestCase

from scrapy import Spider
from scrapy.http.cookies import CookieJar
from scrapy.settings import Settings

from scrapy_cookies.settings import default_settings
from scrapy_cookies.storage.sqlite import SQLiteStorage


class StorageTest(TestCase):

    def setUp(self):
        self.spider = Spider('foo')
        self.settings = Settings()
        self.settings.setmodule(default_settings)

    def tearDown(self):
        pass

    def test_sqlite(self):
        tmpdir = tempfile.mkdtemp()
        local_settings = {
            'COOKIES_STORAGE': 'scrapy_cookies.storage.sqlite.SQLiteStorage',
            'COOKIES_SQLITE_DATABASE': ':memory:',
            'COOKIES_PERSISTENCE': True,
            'COOKIES_PERSISTENCE_DIR': tmpdir + '/cookies'
        }
        settings = deepcopy(self.settings)
        settings.setdict(local_settings)

        storage = SQLiteStorage(settings)
        storage.open_spider(self.spider)

        cookie = storage['no_key']
        self.assertIn('no_key', storage)
        self.assertIsInstance(cookie, CookieJar)
        self.assertEqual(cookie._cookies, CookieJar()._cookies)

        storage['key_1'] = CookieJar()
        self.assertIn('key_1', storage)
        self.assertEqual(storage['key_1']._cookies, CookieJar()._cookies)

        self.assertNotIn('key_2', storage)

        self.assertEqual(len(storage), 2)

        _dict = {'no_key': CookieJar()._cookies,
                 'key_1': CookieJar()._cookies}
        for k, v in storage:
            self.assertDictEqual(v._cookies, _dict[k])

        storage.close_spider(self.spider)
        self.assertTrue(os.path.isfile(tmpdir + '/cookies'))

        storage_2 = SQLiteStorage(settings)
        storage_2.open_spider(self.spider)
        self.assertIn('key_1', storage_2)
        self.assertDictEqual(storage_2['key_1']._cookies, CookieJar()._cookies)

        storage_2.close_spider(self.spider)
        self.assertTrue(os.path.isfile(tmpdir + '/cookies'))
