.. _topics-storage:

=======
Storage
=======

The class of storage is the one implementing MutableMapping_ interface. There
are some storage classes provided with this middleware:

.. _MutableMapping: https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping

.. _storage-inmemory:

InMemoryStorage
---------------

.. module:: scrapy_cookies.storage.in_memory
   :synopsis: In Memory Storage

.. class:: InMemoryStorage

   This storage enables keeping cookies inside the memory, to provide ultra fast
   read and write cookies performance.

.. _storage-sqlite:

SQLiteStorage
-------------

.. module:: scrapy_cookies.storage.sqlite
   :synopsis: SQLite Storage

.. class:: SQLiteStorage

   This storage enables keeping cookies in SQLite, which supports already by
   Python.

The following settings can be used to configure this storage:

* |COOKIES_SQLITE_DATABASE|_

.. |COOKIES_SQLITE_DATABASE| replace:: ``COOKIES_SQLITE_DATABASE``
.. _COOKIES_SQLITE_DATABASE: https://docs.python.org/3/library/sqlite3.html#sqlite3.connect

.. _storage-mongo:

MongoStorage
------------

.. module:: scrapy_cookies.storage.mongo
   :synopsis: Mongo Storage

.. class:: MongoStorage

   This storage enables keeping cookies in MongoDB.

The following settings can be used to configure this storage:

* :setting:`COOKIES_MONGO_MONGOCLIENT_HOST`
* :setting:`COOKIES_MONGO_MONGOCLIENT_PORT`
* :setting:`COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS`
* :setting:`COOKIES_MONGO_MONGOCLIENT_TZ_AWARE`
* :setting:`COOKIES_MONGO_MONGOCLIENT_CONNECT`
* :setting:`COOKIES_MONGO_MONGOCLIENT_KWARGS`
* :setting:`COOKIES_MONGO_DATABASE`
* :setting:`COOKIES_MONGO_COLLECTION`

.. _storage-redis:

RedisStorage
------------

.. module:: scrapy_cookies.storage.redis
   :synopsis: Redis Storage

.. class:: RedisStorage

   This storage enables keeping cookies in Redis.

The following settings can be used to configure this storage:

* :setting:`COOKIES_REDIS_HOST`
* :setting:`COOKIES_REDIS_PORT`
* :setting:`COOKIES_REDIS_DB`
* :setting:`COOKIES_REDIS_PASSWORD`
* :setting:`COOKIES_REDIS_SOCKET_TIMEOUT`
* :setting:`COOKIES_REDIS_SOCKET_CONNECT_TIMEOUT`
* :setting:`COOKIES_REDIS_SOCKET_KEEPALIVE`
* :setting:`COOKIES_REDIS_SOCKET_KEEPALIVE_OPTIONS`
* :setting:`COOKIES_REDIS_CONNECTION_POOL`
* :setting:`COOKIES_REDIS_UNIX_SOCKET_PATH`
* :setting:`COOKIES_REDIS_ENCODING`
* :setting:`COOKIES_REDIS_ENCODING_ERRORS`
* :setting:`COOKIES_REDIS_CHARSET`
* :setting:`COOKIES_REDIS_ERRORS`
* :setting:`COOKIES_REDIS_DECODE_RESPONSES`
* :setting:`COOKIES_REDIS_RETRY_ON_TIMEOUT`
* :setting:`COOKIES_REDIS_SSL`
* :setting:`COOKIES_REDIS_SSL_KEYFILE`
* :setting:`COOKIES_REDIS_SSL_CERTFILE`
* :setting:`COOKIES_REDIS_SSL_CERT_REQS`
* :setting:`COOKIES_REDIS_SSL_CA_CERTS`
* :setting:`COOKIES_REDIS_MAX_CONNECTIONS`

