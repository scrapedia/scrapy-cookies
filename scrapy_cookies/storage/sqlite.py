import io
import logging
import os
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
        if self.database == ':memory:':
            if self.settings['COOKIES_PERSISTENCE'] and os.path.isfile(self.cookies_dir):
                with io.open(self.cookies_dir, 'r') as f:
                    self.cur.executescript(f.read())
                return
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS cookies ('
            'cookiejar_key BLOB PRIMARY KEY UNIQUE, cookiejar BLOB, str TEXT'
            ')'
        )

    def close_spider(self, spider):
        if self.database == ':memory:' and self.settings['COOKIES_PERSISTENCE']:
            with open(self.cookies_dir, 'w') as f:
                for line in self.conn.iterdump():
                    f.write('%s\n' % line)
        self.conn.close()

    def __delitem__(self, v):
        self.cur.execute(
            'DELETE FROM cookies WHERE cookiejar_key=?', pickle.dumps(v)
        )

    def __getitem__(self, k):
        result = self.cur.execute(
            'SELECT cookiejar as "cookiejar [CookieJar]" '
            'FROM cookies '
            'WHERE cookiejar_key=?',
            (pickle.dumps(k),)
        ).fetchone()
        if result:
            return result['cookiejar']
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, k)
        raise KeyError(k)

    def __iter__(self):
        return iter(
            self.cur.execute(
                'SELECT cookiejar_key as "cookiejar_key [CookieJar_key]", cookiejar as "cookiejar [CookieJar]" '
                'FROM cookies'
            ).fetchall()
        )

    def __len__(self):
        return self.cur.execute('SELECT COUNT(*) FROM cookies').fetchone()[0]

    def __setitem__(self, k, v):
        self.cur.execute(
            'INSERT OR REPLACE INTO cookies (cookiejar_key, cookiejar, str) VALUES (?, ?, ?)',
            (pickle.dumps(k), v, str(k))
        )

    def __missing__(self, k):
        v = CookieJar()
        self.__setitem__(k, v)
        return v

    def __contains__(self, k):
        self.cur.execute(
            'SELECT cookiejar as "cookiejar [CookieJar]" '
            'FROM cookies '
            'WHERE cookiejar_key=?',
            (pickle.dumps(k),)
        )
        return bool(self.cur.fetchone())
