.. _intro-installation:

==================
Installation guide
==================

Installing Scrapy
=================

Scrapy-Cookies runs on Python 2.7 and Python 3.4 or above under CPython (default
Python implementation) and PyPy (starting with PyPy 5.9).

You can install Scrapy-Cookies and its dependencies from PyPI with::

    pip install Scrapy-Cookies

We strongly recommend that you install Scrapy and Scrapy-Cookies in
:ref:`a dedicated virtualenv <intro-using-virtualenv>`, to avoid conflicting
with your system packages.

For more detailed and platform specifics instructions, read on.


Things that are good to know
----------------------------

Scrapy-Cookies is written in pure Python and depends on a few key Python
packages (among others):

* `Scrapy`_, of course
* `PyMongo`_
* `redis-py`_
* `ujson`_

The minimal versions which Scrapy-Cookies is tested against are:

* Scrapy 1.5.0

Scrapy-Cookies may work with older versions of these packages but it is not
guaranteed it will continue working because it’s not being tested against them.

.. _Scrapy: https://scrapy.org/
.. _PyMongo: http://api.mongodb.com/python/current/
.. _redis-py: https://redis-py.readthedocs.io/en/latest/
.. _ujson: https://github.com/esnme/ultrajson


.. _intro-using-virtualenv:

Using a virtual environment (recommended)
-----------------------------------------

TL;DR: We recommend installing Scrapy-Cookies inside a virtual environment on
all platforms.

Python packages can be installed either globally (a.k.a system wide), or in
user-space. We do not recommend installing Scrapy and Scrapy-Cookies
system wide.

Instead, we recommend that you install Scrapy and Scrapy-Cookies within a
so-called "virtual environment" (`virtualenv`_). Virtualenvs allow you to not
conflict with already-installed Python system packages (which could break some
of your system tools and scripts), and still install packages normally with
``pip`` (without ``sudo`` and the likes).

To get started with virtual environments, see
`virtualenv installation instructions`_. To install it globally (having it
globally installed actually helps here), it should be a matter of running::

    $ [sudo] pip install virtualenv

Check this `user guide`_ on how to create your virtualenv.

.. note::
    If you use Linux or OS X, `virtualenvwrapper`_ is a handy tool to create
    virtualenvs.

Once you have created a virtualenv, you can install Scrapy-Cookies inside it
with ``pip``, just like any other Python package.
(See :ref:`platform-specific guides <intro-install-platform-notes>`
below for non-Python dependencies that you may need to install beforehand).

Python virtualenvs can be created to use Python 2 by default, or Python 3 by
default.

* If you want to install Scrapy-Cookies with Python 3, install Scrapy-Cookies
  within a Python 3 virtualenv.
* And if you want to install Scrapy-Cookies with Python 2, install
  Scrapy-Cookies within a Python 2 virtualenv.

.. _virtualenv: https://virtualenv.pypa.io
.. _virtualenv installation instructions: https://virtualenv.pypa.io/en/stable/installation/
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
.. _user guide: https://virtualenv.pypa.io/en/stable/userguide/


.. _intro-install-platform-notes:

Platform specific installation notes
====================================

.. _intro-install-windows:

Windows
-------

Same as Scrapy.


.. _intro-install-ubuntu:

Ubuntu 14.04 or above
---------------------

Same as Scrapy.


.. _intro-install-macos:

Mac OS X
--------

Same as Scrapy.


PyPy
----

Same as Scrapy.
