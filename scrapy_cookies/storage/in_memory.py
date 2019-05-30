import io
import logging
import os
import pickle
from collections import UserDict
from typing import Dict

from scrapy.http.cookies import CookieJar
from scrapy.settings import Settings
from scrapy.spiders import Spider
from scrapy.utils.project import data_path

from scrapy_cookies.storage import BaseStorage

logger = logging.getLogger(__name__)


class InMemoryStorage(UserDict, BaseStorage):
    def __init__(self, settings: Settings):
        super(InMemoryStorage, self).__init__()
        self.settings: Settings = settings
        self.cookies_dir: str = data_path(settings["COOKIES_PERSISTENCE_DIR"])

    def open_spider(self, spider: Spider):
        logger.info("COOKIES_PERSISTENCE is %s.", self.settings["COOKIES_PERSISTENCE"])
        if not self.settings["COOKIES_PERSISTENCE"]:
            return
        if not os.path.exists(self.cookies_dir):
            logger.info("Cookies dir does not exist.")
            return
        with io.open(self.cookies_dir, "br") as f:
            self.data: Dict = pickle.load(f)
            logger.info("The number of restored cookies is %d.", len(self.data))

    def close_spider(self, spider: Spider):
        if self.settings["COOKIES_PERSISTENCE"]:
            with io.open(self.cookies_dir, "bw") as f:
                pickle.dump(self.data, f)
                logger.info("The number of saved cookies is %d.", len(self.data))

    def __missing__(self, key) -> CookieJar:
        self.data.update({key: CookieJar()})
        return self.data[key]
