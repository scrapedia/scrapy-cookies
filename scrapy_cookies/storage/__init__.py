from collections.abc import MutableMapping

from scrapy.settings import Settings
from scrapy.spiders import Spider

from scrapy_cookies.downloadermiddlewares.cookies import CookiesMiddleware


class BaseStorage(MutableMapping):
    name = None

    def __init__(self, settings: Settings):
        self.settings: Settings = settings

    @classmethod
    def from_middleware(cls, middleware: CookiesMiddleware):
        obj = cls(middleware.settings)
        return obj

    def open_spider(self, spider: Spider):
        pass

    def close_spider(self, spider: Spider):
        pass

    def __delitem__(self, v):
        pass

    def __getitem__(self, k):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __setitem__(self, k, v):
        pass
