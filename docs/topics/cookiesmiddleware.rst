.. _topics-cookiesmiddleware:

=================
CookiesMiddleware
=================

This is the downloader middleware to inject cookies into requests and extract
cookies from responses.

This middleware mostly inherits the one from Scrapy, which implements the
interface of `downloader middleware`_. With minimum changes, now
it supports the storage class which implements a certain interface (actually
MutableMapping_).

.. _downloader middleware: https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
.. _MutableMapping: https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping
