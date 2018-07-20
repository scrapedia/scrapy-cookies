import pickle
import sqlite3

from scrapy.http.cookies import CookieJar as _CookieJar


class CookieJar(_CookieJar):
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return pickle.dumps(self)
