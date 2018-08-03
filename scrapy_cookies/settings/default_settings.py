COOKIES_ENABLED = True
COOKIES_DEBUG = False

COOKIES_PERSISTENCE = False
COOKIES_PERSISTENCE_DIR = 'cookies'

# ------------------------------------------------------------------------------
# IN MEMORY STORAGE
# ------------------------------------------------------------------------------

COOKIES_STORAGE = 'scrapy_cookies.storage.in_memory.InMemoryStorage'

# ------------------------------------------------------------------------------
# SQLITE STORAGE
# ------------------------------------------------------------------------------

# COOKIES_STORAGE = 'scrapy_cookies.storage.sqlite.SQLiteStorage'
COOKIES_SQLITE_DATABASE = ':memory:'

# ------------------------------------------------------------------------------
# Mongo
# ------------------------------------------------------------------------------

# http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient

# COOKIES_STORAGE = 'scrapy_cookies.storage.mongo.MongoStorage'
COOKIES_MONGO_MONGOCLIENT_HOST = 'localhost'
COOKIES_MONGO_MONGOCLIENT_PORT = 27017
COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS = dict
COOKIES_MONGO_MONGOCLIENT_TZ_AWARE = False
COOKIES_MONGO_MONGOCLIENT_CONNECT = True

COOKIES_MONGO_MONGOCLIENT_KWARGS = {
    # 'username': 'username',
    # 'password': 'password',
    # 'authSource': 'admin',
    # 'authMechanism': 'SCRAM_SHA-1',
}

COOKIES_MONGO_DATABASE = 'cookies'
# or
# COOKIES_MONGO_DATABASE = {
#     'name': 'cookies',
#     'codec_options': None,
#     'read_preference': None,
#     'write_concern': None,
#     'read_concern': None
# }

COOKIES_MONGO_COLLECTION = 'cookies'
# or
# COOKIES_MONGO_COLLECTION = {
#     'name': 'cookies',
#     'codec_options': None,
#     'read_preference': None,
#     'write_concern': None,
#     'read_concern': None
# }
