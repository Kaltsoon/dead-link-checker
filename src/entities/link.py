from dataclasses import dataclass
from typing import TYPE_CHECKING
import re
from pyquery import PyQuery
from utils import url_is_broken

if TYPE_CHECKING:
    from entities.page import Page


@dataclass
class Link:
    html: str
    page: "Page"

    @property
    def href(self) -> str:
        return PyQuery(self.html).attr('href')

    @property
    def text(self) -> str:
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

    async def is_broken(self):
        url = self.url

        if url is None:
            return False

        is_broken = await url_is_broken(url)

        return is_broken

    def __str__(self):
        return self.html
