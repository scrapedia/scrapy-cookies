import logging

import six
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.http import Response
from scrapy.settings import SETTINGS_PRIORITIES
from scrapy.utils.misc import load_object
from scrapy.utils.python import to_native_str

from scrapy_cookies.settings import default_settings, unfreeze_settings

logger = logging.getLogger(__name__)


def format_cookie(cookie):
    # build cookie string
    cookie_str = '{}={}'.format(cookie['name'], cookie['value'])

    if cookie.get('path', None):
        cookie_str += '; Path={}'.format(cookie['path'])
    if cookie.get('domain', None):
        cookie_str += '; Domain={}'.format(cookie['domain'])

    return cookie_str


def get_request_cookies(jar, request):
    if isinstance(request.cookies, dict):
        cookie_list = [{'name': k, 'value': v}
                       for k, v in six.iteritems(request.cookies)]
    else:
        cookie_list = request.cookies

    cookies = [format_cookie(x) for x in cookie_list]
    headers = {'Set-Cookie': cookies}
    response = Response(request.url, headers=headers)

    return jar.make_cookies(response, request)


class CookiesMiddleware(object):
    """This middleware enables working with sites that need cookies"""

    def __init__(self, settings):
        self.settings = settings
        self.jars = load_object(settings['COOKIES_STORAGE']).from_middleware(self)
        self.debug = settings['COOKIES_DEBUG']

    @classmethod
    def from_crawler(cls, crawler):
        with unfreeze_settings(crawler.settings) as settings:
            settings.setmodule(
                module=default_settings, priority=SETTINGS_PRIORITIES['default']
            )
        if not crawler.settings.getbool('COOKIES_ENABLED'):
            raise NotConfigured
        o = cls(crawler.settings)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def spider_opened(self, spider):
        logger.info('%s is used as the cookies storage.',
                    self.settings['COOKIES_STORAGE'])
        self.jars.open_spider(spider)

    def spider_closed(self, spider):
        self.jars.close_spider(spider)

    def process_request(self, request, spider):
        if request.meta.get('dont_merge_cookies', False):
            return

        cookiejar_key = request.meta.get("cookiejar")
        jar = self.jars[cookiejar_key]
        cookies = get_request_cookies(jar, request)
        for cookie in cookies:
            jar.set_cookie_if_ok(cookie, request)
        self.jars[cookiejar_key] = jar

        # set Cookie header
        request.headers.pop('Cookie', None)
        jar.add_cookie_header(request)
        self._debug_cookie(request, spider)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_merge_cookies', False):
            return response

        # extract cookies from Set-Cookie and drop invalid/expired cookies
        cookiejar_key = request.meta.get("cookiejar")
        jar = self.jars[cookiejar_key]
        jar.extract_cookies(response, request)
        self.jars[cookiejar_key] = jar
        self._debug_set_cookie(response, spider)

        return response

    def _debug_cookie(self, request, spider):
        if self.debug:
            cl = [to_native_str(c, errors='replace')
                  for c in request.headers.getlist('Cookie')]
            if cl:
                cookies = "\n".join("Cookie: {}\n".format(c) for c in cl)
                msg = "Sending cookies to: {}\n{}".format(request, cookies)
                logger.debug(msg, extra={'spider': spider})

    def _debug_set_cookie(self, response, spider):
        if self.debug:
            cl = [to_native_str(c, errors='replace')
                  for c in response.headers.getlist('Set-Cookie')]
            if cl:
                cookies = "\n".join("Set-Cookie: {}\n".format(c) for c in cl)
                msg = "Received cookies from: {}\n{}".format(response, cookies)
                logger.debug(msg, extra={'spider': spider})
