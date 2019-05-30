import logging
import pickle
import re
from itertools import starmap
from typing import Dict

import ujson
from redis.client import Redis
from scrapy.http.cookies import CookieJar
from scrapy.settings import Settings
from scrapy.spiders import Spider

from scrapy_cookies.storage import BaseStorage

logger = logging.getLogger(__name__)
pattern = re.compile("^COOKIES_REDIS_(?P<kwargs>(?!KWARGS).*)$")


def get_arguments(var):
    return {str: {"name": var}, dict: var}[type(var)]


def write_cookiejar(cookiejar):
    return {
        "cookiejar": pickle.dumps(cookiejar),
        "cookies": ujson.dumps(cookiejar._cookies),
    }


def read_cookiejar(document):
    try:
        return pickle.loads(document["cookiejar"])
    except (TypeError, KeyError):
        return None


class RedisStorage(BaseStorage):
    def __init__(self, settings: Settings):
        super(RedisStorage, self).__init__(settings)
        self.redis_settings: Dict[str, str] = dict(
            starmap(
                lambda k, v: (pattern.sub(lambda x: x.group(1).lower(), k), v),
                filter(
                    lambda pair: pattern.match(pair[0]), settings.copy_to_dict().items()
                ),
            )
        )
        self.r: Redis = None

    @classmethod
    def from_middleware(cls, middleware):
        obj = cls(middleware.settings)
        return obj

    def open_spider(self, spider: Spider):
        self.r: Redis = Redis(**self.redis_settings)

    def close_spider(self, spider: Spider):
        pass

    def __missing__(self, k) -> CookieJar:
        cookiejar: CookieJar = CookieJar()
        self[k] = cookiejar
        return cookiejar

    def __delitem__(self, v):
        self.r.delete(v)

    def __getitem__(self, k) -> CookieJar:
        v: CookieJar = read_cookiejar(self.r.hgetall(k))
        if isinstance(v, CookieJar):
            return v
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, k)
        raise KeyError(k)

    def __iter__(self):
        return self.r.scan_iter()

    def __len__(self) -> int:
        return self.r.dbsize()

    def __setitem__(self, k, v: CookieJar):
        self.r.hmset(name=k, mapping=write_cookiejar(v))
