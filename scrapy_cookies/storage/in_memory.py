from collections import defaultdict

from scrapy.http.cookies import CookieJar


class InMemoryStorage(defaultdict):
    def __init__(self, settings):
        super(InMemoryStorage, self).__init__(CookieJar)
        self.settings = settings
