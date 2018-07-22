import logging
import pickle
import sqlite3

from scrapy.http.cookies import CookieJar
from scrapy.utils.project import data_path

from scrapy_cookies.storage import BaseStorage

logger = logging.getLogger(__name__)


def adapt_cookiejar(cookiejar):
    return pickle.dumps(cookiejar)


def convert_cookiejar_and_its_key(cookiejar_or_its_key):
    return pickle.loads(cookiejar_or_its_key)


sqlite3.register_adapter(CookieJar, adapt_cookiejar)
sqlite3.register_converter('cookiejar', convert_cookiejar_and_its_key)
sqlite3.register_converter('cookiejar_key', convert_cookiejar_and_its_key)


class SQLiteStorage(BaseStorage):
    def __init__(self, settings):
        super(SQLiteStorage, self).__init__(settings)
        self.cookies_dir = data_path(settings['COOKIES_PERSISTENCE_DIR'])
        self.database = settings['COOKIES_SQLITE_DATABASE']
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        self.conn = sqlite3.connect(
            self.database,
            detect_types=sqlite3.PARSE_COLNAMES,
            isolation_level=None)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS cookies ('
            'cookiejar_key BLOB PRIMARY KEY UNIQUE, cookiejar BLOB, str TEXT'
            ')'
        )

    def close_spider(self, spider):
        self.conn.close()
