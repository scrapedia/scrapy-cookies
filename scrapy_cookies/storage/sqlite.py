import pickle
import sqlite3

from scrapy.http.cookies import CookieJar


def adapt_cookiejar(cookiejar):
    return pickle.dumps(cookiejar)


def convert_cookiejar_and_its_key(cookiejar_or_its_key):
    return pickle.loads(cookiejar_or_its_key)


sqlite3.register_adapter(CookieJar, adapt_cookiejar)
sqlite3.register_converter('cookiejar', convert_cookiejar_and_its_key)
sqlite3.register_converter('cookiejar_key', convert_cookiejar_and_its_key)
