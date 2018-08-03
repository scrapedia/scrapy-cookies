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
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_PORT

COOKIES_MONGO_MONGOCLIENT_PORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS

COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_TZ_AWARE

COOKIES_MONGO_MONGOCLIENT_TZ_AWARE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_CONNECT

COOKIES_MONGO_MONGOCLIENT_CONNECT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_MONGOCLIENT_KWARGS

COOKIES_MONGO_MONGOCLIENT_KWARGS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_DATABASE

COOKIES_MONGO_DATABASE
~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.

.. setting:: COOKIES_MONGO_COLLECTION

COOKIES_MONGO_COLLECTION
~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to mongo_client_.


.. _mongo_client: http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
