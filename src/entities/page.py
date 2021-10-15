from pyquery import PyQuery
from urllib.parse import urlparse
from entities.link import Link


def get_base_url(url):
    uri = urlparse(url)

    return f'{uri.scheme}://{uri.netloc}'


class Page:
    def __init__(self, url):
        self.url = url
        self._query = PyQuery(url=url)

    @property
    def base_url(self):
        return get_base_url(self.url)

    @property
    def links(self):
        anchors = self._query('a')
        links = []

        for anchor in anchors:
            anchor_html = PyQuery(anchor).outerHtml()
            link = Link(anchor_html, self)

            if (link.href and link.text):
                links.append(link)

        return links
