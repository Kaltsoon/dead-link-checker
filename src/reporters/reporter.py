from scraper import Scraper

class Reporter:
    def produce_report(self, scraper: Scraper) -> None:
        raise NotImplementedError()
