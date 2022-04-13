from dataclasses import dataclass, field
from typing import Dict, List
import json
from reporters.reporter import Reporter
from scraper import Scraper
from loggers.logger import Logger
from loggers.nop_logger import NopLogger


@dataclass
class FileReporter(Reporter):
    path: str
    logger: Logger = field(default_factory=NopLogger)

    def produce_report(self, scraper: Scraper) -> None:
        broken_links = scraper.get_broken_links()

        link_dict: Dict[str, List[str]] = {}

        for link in broken_links:
            link_dict[link.page.url] = link_dict.get(link.page.url, [])
            link_dict[link.page.url].append(link.html)

        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(link_dict, indent=2))

        urls = link_dict.keys()

        self.logger.success(
            f'Scraping is done! Found {len(broken_links)} links in {len(urls)} pages. Report can be found in {self.path}'  # pylint: disable=line-too-long
        )
