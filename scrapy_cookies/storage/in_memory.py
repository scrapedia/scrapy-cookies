from collections import defaultdict

from scrapy.http.cookies import CookieJar


class InMemoryStorage(defaultdict):
    def __init__(self, settings):
        super(InMemoryStorage, self).__init__(CookieJar)
        self.settings = settings

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
