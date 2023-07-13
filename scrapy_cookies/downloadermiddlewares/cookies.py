import logging
from http.cookiejar import Cookie
from typing import Dict, List

from scrapy.crawler import Crawler
from scrapy.exceptions import NotConfigured
from scrapy.http import Request, Response
from scrapy.http.cookies import CookieJar
from scrapy.settings import SETTINGS_PRIORITIES, Settings
from scrapy.signals import spider_closed, spider_opened
from scrapy.spiders import Spider
from scrapy.utils.misc import load_object
try:
    from scrapy.utils.python import to_native_str
except ImportError:
    # to_native_str is deprecated since version 2.8
    # https://docs.scrapy.org/en/2.8/news.html#deprecation-removals
    from scrapy.utils.python import to_unicode as to_native_str

from scrapy_cookies.settings import default_settings, unfreeze_settings

logger = logging.getLogger(__name__)


def format_cookie(cookie: Dict) -> str:
    # build cookie string
    cookie_str: str = "{}={}".format(cookie["name"], cookie["value"])

    if cookie.get("path", None):
        cookie_str += "; Path={}".format(cookie["path"])
    if cookie.get("domain", None):
        cookie_str += "; Domain={}".format(cookie["domain"])

    return cookie_str


def get_request_cookies(jar: CookieJar, request: Request) -> List[Cookie]:
    if isinstance(request.cookies, dict):
        cookie_list: List[Dict] = [
            {"name": k, "value": v} for k, v in request.cookies.items()
        ]
    else:
        cookie_list: List[Dict] = request.cookies

    cookies: List[str] = [format_cookie(x) for x in cookie_list]
    headers: Dict[str, List[str]] = {"Set-Cookie": cookies}
    response: Response = Response(request.url, headers=headers)

    return jar.make_cookies(response, request)


class CookiesMiddleware:
    """This middleware enables working with sites that need cookies"""

    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self.jars = load_object(settings["COOKIES_STORAGE"]).from_middleware(self)
        self.debug: bool = settings["COOKIES_DEBUG"]

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        with unfreeze_settings(crawler.settings) as settings:
            settings.setmodule(
                module=default_settings, priority=SETTINGS_PRIORITIES["default"]
            )
        if not crawler.settings.getbool("COOKIES_ENABLED"):
            raise NotConfigured
        obj = cls(crawler.settings)
        crawler.signals.connect(obj.spider_opened, signal=spider_opened)
        crawler.signals.connect(obj.spider_closed, signal=spider_closed)
        return obj

    def spider_opened(self, spider: Spider):
        logger.info(
            "%s is used as the cookies storage.", self.settings["COOKIES_STORAGE"]
        )
        self.jars.open_spider(spider)

    def spider_closed(self, spider: Spider):
        self.jars.close_spider(spider)

    def process_request(self, request: Request, spider: Spider) -> None:
        if request.meta.get("dont_merge_cookies", False):
            return

        cookiejar_key = request.meta.get("cookiejar")
        jar: CookieJar = self.jars[cookiejar_key]
        cookies: List[Cookie] = get_request_cookies(jar, request)
        for cookie in cookies:
            jar.set_cookie_if_ok(cookie, request)
        self.jars[cookiejar_key] = jar

        # set Cookie header
        request.headers.pop("Cookie", None)
        jar.add_cookie_header(request)
        self._debug_cookie(request, spider)

    def process_response(
        self, request: Request, response: Response, spider: Spider
    ) -> Response:
        if request.meta.get("dont_merge_cookies", False):
            return response

        # extract cookies from Set-Cookie and drop invalid/expired cookies
        cookiejar_key = request.meta.get("cookiejar")
        jar: CookieJar = self.jars[cookiejar_key]
        jar.extract_cookies(response, request)
        self.jars[cookiejar_key] = jar
        self._debug_set_cookie(response, spider)

        return response

    def _debug_cookie(self, request: Request, spider: Spider):
        if self.debug:
            cl = [
                to_native_str(c, errors="replace")
                for c in request.headers.getlist("Cookie")
            ]
            if cl:
                cookies: str = "\n".join("Cookie: {}\n".format(c) for c in cl)
                msg: str = "Sending cookies to: {}\n{}".format(request, cookies)
                logger.debug(msg, extra={"spider": spider})

    def _debug_set_cookie(self, response: Response, spider: Spider):
        if self.debug:
            cl = [
                to_native_str(c, errors="replace")
                for c in response.headers.getlist("Set-Cookie")
            ]
            if cl:
                cookies: str = "\n".join("Set-Cookie: {}\n".format(c) for c in cl)
                msg: str = "Received cookies from: {}\n{}".format(response, cookies)
                logger.debug(msg, extra={"spider": spider})
