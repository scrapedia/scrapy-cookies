.. _topic-settings:

========
Settings
========

The default settings of this middleware keeps the same behaviour as the one in
Scrapy.

As an enhancement, there are some settings added in this middleware:

.. setting:: COOKIES_PERSISTENCE

COOKIES_PERSISTENCE
~~~~~~~~~~~~~~~~~~~

Default: ``False``

Whether to enable this cookies middleware save the cookies on disk. If disabled,
no cookies will be saved on disk.

Notice that this setting only affects when the storage uses memory as cookies
container.

.. setting:: COOKIES_DEBUG

COOKIES_PERSISTENCE_DIR
~~~~~~~~~~~~~~~~~~~~~~~

Default: ``cookies``

When ``COOKIES_PERSISTENCE`` is True, the storage which use memory as cookies
container will save the cookies in the file ``cookies`` under the folder
``.scrapy`` in your project, while if the storage does not use memory as cookies
container will not affect by this setting.

.. setting:: COOKIES_STORAGE

COOKIES_STORAGE
~~~~~~~~~~~~~~~

Default: ``scrapy_cookies.storage.in_memory.InMemoryStorage``

With this setting, the storage can be specified. There are some storage classes
provided with this middleware by default:

* :ref:`scrapy_cookies.storage.in_memory.InMemoryStorage<storage-inmemory>`
* :ref:`scrapy_cookies.storage.sqlite.SQLiteStorage<storage-sqlite>`
* :ref:`scrapy_cookies.storage.mongo.MongoStorage<storage-mongo>`

.. setting:: COOKIES_MONGO_MONGOCLIENT_HOST

COOKIES_MONGO_MONGOCLIENT_HOST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``localhost``

Hostname or IP address or Unix domain socket path of a single mongod or mongos
instance to connect to, or a mongodb URI, or a list of hostnames / mongodb URIs.
If host is an IPv6 literal it must be enclosed in ‘[‘ and ‘]’ characters
following the RFC2732 URL syntax (e.g. ‘[::1]’ for localhost). Multihomed and
round robin DNS addresses are not supported.

Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_PORT

COOKIES_MONGO_MONGOCLIENT_PORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``27017``

Port number on which to connect.

Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS

COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``dict``

Default class to use for documents returned from queries on this client.

Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_TZ_AWARE

COOKIES_MONGO_MONGOCLIENT_TZ_AWARE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``False``

If True, datetime instances returned as values in a document by this MongoClient
will be timezone aware (otherwise they will be naive).

Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_CONNECT

COOKIES_MONGO_MONGOCLIENT_CONNECT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``True``

If True (the default), immediately begin connecting to MongoDB in the
background. Otherwise connect on the first operation.

Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_KWARGS

COOKIES_MONGO_MONGOCLIENT_KWARGS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_DATABASE

COOKIES_MONGO_DATABASE
~~~~~~~~~~~~~~~~~~~~~~

Default: ``cookies``

The name of the database - a string. If None (the default) the database named in
the MongoDB connection URI is returned.

Please refer to get_database_.

.. setting:: COOKIES_MONGO_COLLECTION

COOKIES_MONGO_COLLECTION
~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``cookies``

The name of the collection - a string.

Please refer to get_collection_.


.. _mongo_client: http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
.. _get_database: http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient.get_database
.. _get_collection: http://api.mongodb.com/python/current/api/pymongo/database.html#pymongo.database.Database.get_collection
