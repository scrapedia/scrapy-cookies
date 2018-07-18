import logging
from collections import MutableMapping


class BaseStorage(MutableMapping):
    name = None

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_middleware(cls, middleware):
        return cls(middleware.settings)

    @property
    def logger(self):
        logger = logging.getLogger(self.name)
        return logging.LoggerAdapter(logger, {'storage': self})

    def log(self, message, level=logging.DEBUG, **kw):
        """Log the given message at the given log level

        This helper wraps a log call to the logger within the storage, but you
        can use it directly (e.g. Storage.logger.info('msg')) or use any other
        Python logger too.
        """
        self.logger.log(level, message, **kw)

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
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
