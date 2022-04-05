from dataclasses import dataclass
from typing import List
from pyquery import PyQuery
from entities.link import Link
from utils import get_base_url


@dataclass
class Page:
    url: str

    def __post_init__(self):
        try:
            self._query = PyQuery(url=self.url)
        except Exception: # pylint: disable=broad-except
            self._query = None

    @property
    def base_url(self):
        return get_base_url(self.url)

    @property
    def links(self):
        if self._query is None:
            return []

        anchors = self._query('a')
        links: List[Link] = []

        for anchor in anchors:
            anchor_html = PyQuery(anchor).outerHtml() #pylint: disable=no-member
            link = Link(anchor_html, self)

            if (link.href and link.text):
                links.append(link)

        return links
