from pyquery import PyQuery
from entities.link import Link
from utils import get_base_url


class Page:
    def __init__(self, url):
        self.url = url
        self._query = None

        self.initialize()

    def initialize(self):
        try:
            self._query = PyQuery(url=self.url)
        except:
            pass

    @property
    def base_url(self):
        return get_base_url(self.url)

    @property
    def links(self):
        if self._query is None:
            return []

        anchors = self._query('a')
        links = []

        for anchor in anchors:
            anchor_html = PyQuery(anchor).outerHtml()
            link = Link(anchor_html, self)

            if (link.href and link.text):
                links.append(link)

        return links
