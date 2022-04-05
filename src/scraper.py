from dataclasses import dataclass, field
from typing import List
import asyncio
from loggers.logger import Logger
from loggers.nop_logger import NopLogger
from entities.page import Page
from entities.link import Link
from utils import get_url_without_fragment


async def get_broken_status(links):
    results = await asyncio.gather(*[link.is_broken() for link in links], return_exceptions=True)

    return results


@dataclass
class Scraper:
    url: str
    max_depth: int = field(default=10)
    logger: Logger = field(default_factory=NopLogger)

    def __post_init__(self):
        self._visited = {}

    def get_broken_links(self):
        normalized_url = get_url_without_fragment(self.url)

        links: List[Link] = self._scrape_page(Page(normalized_url))

        return links

    def _url_is_visited(self, url):
        normalized_url = get_url_without_fragment(url)

        return self._visited.get(normalized_url) is not None

    def _set_url_visited(self, url):
        normalized_url = get_url_without_fragment(url)

        self._visited[normalized_url] = True

    def _should_scrape_link(self, link):
        return link.is_internal() and not self._url_is_visited(link.url)

    def _scrape_page(self, page, depth=0):
        self.logger.info(f'Going through links at {page.url}...')

        self._set_url_visited(page.url)

        broken_links = []
        links = page.links

        results = asyncio.run(get_broken_status(links))

        for link, is_broken in zip(links, results):
            if is_broken:
                broken_links.append(link)

        if broken_links:
            self.logger.warning(
                f'Found {len(broken_links)} broken links at {page.url}'
            )
        else:
            self.logger.success(f'Found no broken links at {page.url}')

        if depth >= self.max_depth:
            return broken_links

        for link, is_broken in zip(links, results):
            if self._should_scrape_link(link):
                normalized_url = get_url_without_fragment(link.url)

                broken_links = broken_links + \
                    self._scrape_page(Page(normalized_url), depth + 1)

        return broken_links
