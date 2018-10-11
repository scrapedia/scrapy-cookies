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
# MONGODB
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

# ------------------------------------------------------------------------------
# REDIS STORAGE
# ------------------------------------------------------------------------------

# COOKIES_STORAGE = 'scrapy_cookies.storage.redis.RedisStorage'
COOKIES_REDIS_HOST = 'localhost'
COOKIES_REDIS_PORT = 6379
COOKIES_REDIS_DB = 0
COOKIES_REDIS_PASSWORD = None
COOKIES_REDIS_SOCKET_TIMEOUT = None
COOKIES_REDIS_SOCKET_CONNECT_TIMEOUT = None
COOKIES_REDIS_SOCKET_KEEPALIVE = None
COOKIES_REDIS_SOCKET_KEEPALIVE_OPTIONS = None
COOKIES_REDIS_CONNECTION_POOL = None
COOKIES_REDIS_UNIX_SOCKET_PATH = None
COOKIES_REDIS_ENCODING = 'utf-8'
COOKIES_REDIS_ENCODING_ERRORS = 'strict'
COOKIES_REDIS_CHARSET = None
COOKIES_REDIS_ERRORS = None
COOKIES_REDIS_DECODE_RESPONSES = True
COOKIES_REDIS_RETRY_ON_TIMEOUT = False
COOKIES_REDIS_SSL = False
COOKIES_REDIS_SSL_KEYFILE = None
COOKIES_REDIS_SSL_CERTFILE = None
COOKIES_REDIS_SSL_CERT_REQS = None
COOKIES_REDIS_SSL_CA_CERTS = None
COOKIES_REDIS_MAX_CONNECTIONS = None
