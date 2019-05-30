from os.path import dirname, join

from setuptools import find_packages, setup

with open(join(dirname(__file__), "scrapy_cookies/VERSION"), "rb") as f:
    version = f.read().decode("ascii").strip()


extras_require = {}

setup(
    name="Scrapy-Cookies",
    version=version,
    url="https://github.com/grammy-jiang/scrapy-cookies",
    description="A middleware of cookies persistence for Scrapy",
    long_description=open("README.rst").read(),
    author="Scrapedia",
    author_email="Scrapedia@outlook.com",
    maintainer="Scrapedia",
    maintainer_email="Scrapedia@outlook.com",
    license="BSD",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=["hiredis", "pymongo", "redis", "scrapy", "ujson"],
    extras_require=extras_require,
)
