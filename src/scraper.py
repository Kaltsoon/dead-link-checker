from loggers.nop_logger import NopLogger
from entities.page import Page
from utils import get_url_without_fragment


class Scraper:
    def __init__(self, url, logger=NopLogger(), max_depth=10):
        self.url = url
        self._visited = {}
        self._max_depth = max_depth
        self._logger = logger

    def get_broken_links(self):
        normalized_url = get_url_without_fragment(self.url)

        return self._scrape_page(Page(normalized_url))

    def _url_is_visited(self, url):
        normalized_url = get_url_without_fragment(url)

        return self._visited.get(normalized_url) is not None

    def _set_url_visited(self, url):
        normalized_url = get_url_without_fragment(url)

        self._visited[normalized_url] = True

    def _should_scrape_link(self, link):
        return link.is_internal() and not self._url_is_visited(link.url) and not link.is_broken()

    def _scrape_page(self, page, depth=0):
        self._logger.info(f'Going through links at {page.url}...')

        self._set_url_visited(page.url)

        broken_links = []
        links = page.links

        for link in links:
            if link.is_broken():
                broken_links.append(link)

        if broken_links:
            self._logger.warning(
                f'Found {len(broken_links)} broken links at {page.url}'
            )
        else:
            self._logger.success(f'Found no broken links at {page.url}')

        if depth >= self._max_depth:
            return broken_links

        for link in links:
            if self._should_scrape_link(link):
                normalized_url = get_url_without_fragment(link.url)

                broken_links = broken_links + \
                    self._scrape_page(Page(normalized_url), depth + 1)

        return broken_links
