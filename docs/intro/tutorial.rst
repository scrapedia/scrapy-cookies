.. _intro-tutorial:

=======================
Scrapy-Cookies Tutorial
=======================

In this tutorial, we'll assume that Scrapy-Cookies is already installed on your
system. If that's not the case, see :ref:`intro-installation`.

This tutorial will walk you through these tasks:

1. Use various storage classes in this middleware
2. Save cookies on disk


Use various storage classes in this middleware
==============================================

Before you start scraping, just put the following code into your settings.py::

    DOWNLOADER_MIDDLEWARES.update({
        'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
        'scrapy_cookies.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    })

With the default settings of this middleware, a in-memory storage will be used.

There is a storage named SQLiteStorage. If you want to use it instead of the
in-memory one, simple put the following code below the previous one::

    COOKIES_STORAGE = 'scrapy_cookies.storage.sqlite.SQLiteStorage'
    COOKIES_SQLITE_DATABASE = ':memory:'

There is also one storage named MongoStorage. If you want to use it instead of
the in-memory one, simple put the following code below the previous one::

    COOKIES_STORAGE = 'scrapy_cookies.storage.mongo.MongoStorage'

    COOKIES_MONGO_MONGOCLIENT_HOST = 'localhost'
    COOKIES_MONGO_MONGOCLIENT_PORT = 27017
    COOKIES_MONGO_MONGOCLIENT_DOCUMENT_CLASS = dict
    COOKIES_MONGO_MONGOCLIENT_TZ_AWARE = False
    COOKIES_MONGO_MONGOCLIENT_CONNECT = True

    COOKIES_MONGO_MONGOCLIENT_KWARGS = {
        'username': 'username',
        'password': 'password',
    }

    COOKIES_MONGO_DATABASE = 'cookies'
    COOKIES_MONGO_COLLECTION = 'cookies'

When you implement your own storage, you can set ``COOKIES_STORAGE`` to your own
one.


Save cookies and restore in your next run
=========================================

By default this middleware would not save the cookies. When you need to keep
the cookies for further usage, for example a login cookie, you wish to save the
cookies on disk for next run.

This middleware provides this ability with one setting::

    COOKIES_PERSISTENCE = True

Most of time the file saved cookies is named ``cookies`` under the folder
``.scrapy``. If you want to change it, use this setting::

    COOKIES_PERSISTENCE_DIR = 'your-cookies-path'

After these settings, this middleware would load the previous saved cookies in
the next run.

.. note:: Please keep the storage is the same class when you want save the
  cookies and restore them. The cookies persistence file is not compatible
  between different storage classes.

.. note:: This feature will depend on the storage class used

Next steps
==========

This tutorial covered only the basics of Scrapy-Cookies, but there's a lot of
other features not mentioned here. Check the :ref:`topics-whatelse` section in
:ref:`intro-overview` chapter for a quick overview of the most important ones.

You can continue from the section :ref:`section-basics` to know more about this
middleware, storage and other things this tutorial hasn't covered. If you prefer
to play with an example project, check the :ref:`intro-examples` section.
