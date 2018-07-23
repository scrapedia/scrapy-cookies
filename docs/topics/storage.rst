.. _topics-storage:

=======
Storage
=======

The class of storage is the one implementing MutableMapping_ interface. There
are some storage classes provided with this middleware:

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

* |COOKIES_SQLITE_DATABASE|_.

.. _MutableMapping: https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping

.. |COOKIES_SQLITE_DATABASE| replace:: ``COOKIES_SQLITE_DATABASE``
.. _COOKIES_SQLITE_DATABASE: https://docs.python.org/3/library/sqlite3.html#sqlite3.connect

