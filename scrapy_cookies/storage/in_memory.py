from collections import defaultdict

from scrapy.http.cookies import CookieJar

from scrapy_cookies.storage import BaseStorage


class InMemoryStorage(defaultdict, BaseStorage):
    def __init__(self, settings):
        super(InMemoryStorage, self).__init__(CookieJar)
        self.settings = settings
