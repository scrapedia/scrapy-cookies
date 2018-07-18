import io
import os
import pickle
from collections import defaultdict

from scrapy.http.cookies import CookieJar
from scrapy.utils.project import data_path

from scrapy_cookies.storage import BaseStorage


class InMemoryStorage(defaultdict, BaseStorage):
    def __init__(self, settings):
        super(InMemoryStorage, self).__init__(CookieJar)
        self.settings = settings

    @classmethod
    def from_middleware(cls, middleware):
        settings = middleware.settings

        if not settings['COOKIES_PERSISTENCE']:
            return cls(settings)
        cookies_dir = data_path(settings['COOKIES_PERSISTENCE_DIR'])
        if not os.path.exists(cookies_dir):
            return cls(settings)
        with io.open(cookies_dir, 'br') as f:
            return pickle.load(f)

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        if not self.settings['COOKIES_PERSISTENCE']:
            return
        cookies_dir = data_path(self.settings['COOKIES_PERSISTENCE_DIR'])
        with io.open(cookies_dir, 'bw') as f:
            pickle.dump(self, f)

