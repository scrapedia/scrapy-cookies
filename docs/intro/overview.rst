.. _intro-overview:

==========================
Scrapy-Cookies at a glance
==========================

Scrapy-Cookies is a downloader middleware for Scrapy.

Even though Scrapy-Cookies was originally designed for cookies save and restore
(manage the login session), it can also be used to share cookies between various
spider nodes.


Walk-through of an example spider
=================================

In order to show you what Scrapy-Cookies brings to the table, we'll walk you
through an example of a Scrapy project's settings with Scrapy-Cookies using the
simplest way to save and restore the cookies.

Here's the code for settings that uses in memory as storage::

    DOWNLOADER_MIDDLEWARES.update({
        'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
        'scrapy_cookies.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    })

    COOKIES_ENABLED = True

    COOKIES_PERSISTENCE = True
    COOKIES_PERSISTENCE_DIR = 'cookies'

    # ------------------------------------------------------------------------------
    # IN MEMORY STORAGE
    # ------------------------------------------------------------------------------

    COOKIES_STORAGE = 'scrapy_cookies.storage.in_memory.InMemoryStorage'

Put this in your project's settings, and run your spider.

When this finishes you will have a ``cookies`` file in the folder ``.scrapy``
under your project folder. The file ``cookies`` is the pickled object contained
cookies from your spider.


What just happened?
-------------------

When you run your spider, this middleware initializes all objects related to
maintaining cookies.

The crawl starts to send requests and receive responses, at the same time this
middleware extracts and sets the cookies from and to requests and responses.

When the spider stopped, this middleware will save the cookies to the path
defined in ``COOKIES_PERSISTENCE_DIR``.


.. _topics-whatelse:

What else?
==========

You've seen how to save and store cookies with Scrapy-Cookies. And this
middleware provides an interface to let you customize your own cookies storage
ways, such as:


* In-memory storage, with ultra-fast speed to process

* SQLite storage, with ultra-fast speed when uses memory database, and easy to
  read and sharing with other process on disk databases

* Other database like MongoDB, MySQL, even HBase to integrate with other
  programmes across your


What's next?
============

The next steps for you are to
:ref:`install Scrapy-Cookies <intro-installation>`,
:ref:`follow through the tutorial <intro-tutorial>` to learn how to create
a project with Scrapy-Cookies and `join the community`_. Thanks for your
interest!

.. _join the community: https://scrapy.org/community/
