import io
import logging
import os
import pickle

from scrapy.http.cookies import CookieJar
from scrapy.utils.project import data_path
from six.moves import UserDict

from scrapy_cookies.storage import BaseStorage

logger = logging.getLogger(__name__)


class InMemoryStorage(UserDict, BaseStorage):
    def __init__(self, settings):
        super(InMemoryStorage, self).__init__()
        self.settings = settings
        self.cookies_dir = data_path(settings['COOKIES_PERSISTENCE_DIR'])

    def open_spider(self, spider):
        logger.info('COOKIES_PERSISTENCE is %s.',
                    self.settings['COOKIES_PERSISTENCE'])
        if not self.settings['COOKIES_PERSISTENCE']:
            return
        if not os.path.exists(self.cookies_dir):
            logger.info('Cookies dir does not exist.')
            return
        with io.open(self.cookies_dir, 'br') as f:
            self.data = pickle.load(f)
            logger.info('The number of restored cookies is %d.', len(self.data))

    def close_spider(self, spider):
        if self.settings['COOKIES_PERSISTENCE']:
            with io.open(self.cookies_dir, 'bw') as f:
                pickle.dump(self.data, f)
                logger.info('The number of saved cookies is %d.', len(self.data))

    def __missing__(self, key):
        self.data.update({key: CookieJar()})
        return self.data[key]
