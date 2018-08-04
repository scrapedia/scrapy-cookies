import logging
import pickle
import re
from itertools import starmap

import ujson
from redis.client import Redis
from scrapy.http.cookies import CookieJar

from scrapy_cookies.storage import BaseStorage

logger = logging.getLogger(__name__)
pattern = re.compile('^COOKIES_REDIS_(?P<kwargs>(?!KWARGS).*)$')


def get_arguments(var):
    return {str: {'name': var}, dict: var}[type(var)]


def write_cookiejar(cookiejar):
    return {'cookiejar': pickle.dumps(cookiejar),
            'cookies': ujson.dumps(cookiejar._cookies)}


def read_cookiejar(document):
    try:
        return pickle.loads(document['cookiejar'])
    except (TypeError, KeyError):
        return None


class RedisStorage(BaseStorage):
    def __init__(self, settings):
        super(RedisStorage, self).__init__(settings)
        self.redis_settings = dict(starmap(
            lambda k, v: (pattern.sub(lambda x: x.group(1).lower(), k), v),
            filter(lambda pair: pattern.match(pair[0]),
                   settings.copy_to_dict().items())
        ))
        self.r = None

    @classmethod
    def from_middleware(cls, middleware):
        return cls(middleware.settings)

    def open_spider(self, spider):
        self.r = Redis(**self.redis_settings)

    def close_spider(self, spider):
        pass

    def __missing__(self, k):
        cookiejar = CookieJar()
        self[k] = cookiejar
        return cookiejar

    def __delitem__(self, v):
        self.r.delete(v)

    def __getitem__(self, k):
        v = read_cookiejar(self.r.hgetall(k))
        if isinstance(v, CookieJar):
            return v
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, k)
        raise KeyError(k)

    def __iter__(self):
        return self.r.scan_iter()

    def __len__(self):
        return self.r.dbsize()

    def __setitem__(self, k, v):
        self.r.hmset(k, write_cookiejar(v))
