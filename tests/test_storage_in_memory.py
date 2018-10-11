import os
import tempfile
from copy import deepcopy
from unittest import TestCase

from scrapy import Spider
from scrapy.http.cookies import CookieJar
from scrapy.settings import Settings

from scrapy_cookies.settings import default_settings
from scrapy_cookies.storage.in_memory import InMemoryStorage


class StorageTest(TestCase):

    def setUp(self):
        self.spider = Spider('foo')
        self.settings = Settings()
        self.settings.setmodule(default_settings)

    def tearDown(self):
        pass

    def test_in_memory(self):
        tmpdir = tempfile.mkdtemp()
        local_settings = {
            'COOKIES_PERSISTENCE': True,
            'COOKIES_PERSISTENCE_DIR': tmpdir + '/cookies'
        }
        settings = deepcopy(self.settings)
        settings.setdict(local_settings)

        storage = InMemoryStorage(settings)
        storage.open_spider(self.spider)

        cookie = storage['no_key']
        self.assertIsInstance(cookie, CookieJar)
        self.assertDictEqual(cookie._cookies, CookieJar()._cookies)

        storage['key_1'] = CookieJar()
        self.assertIn('key_1', storage)
        self.assertEqual(storage['key_1']._cookies, CookieJar()._cookies)

        storage.close_spider(self.spider)
        self.assertTrue(os.path.isfile(tmpdir + '/cookies'))
