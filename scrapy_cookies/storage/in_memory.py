import io
import os
import pickle

from scrapy.http.cookies import CookieJar
from scrapy.utils.project import data_path
from six.moves import UserDict

from scrapy_cookies.storage import BaseStorage


class InMemoryStorage(UserDict, BaseStorage):
    def __init__(self, settings):
        super(InMemoryStorage, self).__init__()
        self.settings = settings
        self.cookies_dir = data_path(settings['COOKIES_PERSISTENCE_DIR'])

    def open_spider(self, spider):
        if not self.settings['COOKIES_PERSISTENCE']:
            return
        if not os.path.exists(self.cookies_dir):
            return
        with io.open(self.cookies_dir, 'br') as f:
            self.data = pickle.load(f)

    def close_spider(self, spider):
        if self.settings['COOKIES_PERSISTENCE']:
            with io.open(self.cookies_dir, 'bw') as f:
                pickle.dump(self.data, f)

    def __missing__(self, key):
        self.data.update({key: CookieJar()})
        return self.data[key]
