import re
import requests
from pyquery import PyQuery


class Link:
    def __init__(self, html, page):
        self.html = html
        self.page = page

    @property
    def href(self):
        return PyQuery(self.html).attr('href')

    @property
    def text(self):
        return PyQuery(self.html).text()

    @property
    def url(self):
        href = self.href

        if href is None:
            return None

        if re.match(r'^https?://', href):
            return href

        if href.startswith('/'):
            return f'{self.page.base_url}{href}'

        return None

    def is_internal(self):
        url = self.url

        if url is None:
            return False

        return url.startswith(self.page.base_url)

    def is_broken(self):
        url = self.url

        if url is None:
            return False

        respose = requests.get(url, timeout=10)

        return respose.status_code != requests.codes.ok

    def __str__(self):
        return self.html
