import json
from reporters.reporter import Reporter


class FileReporter(Reporter):
    def __init__(self, path):
        self.path = path

    def produce_report(self, scraper):
        broken_links = scraper.get_broken_links()

        link_dict = {}

        for link in broken_links:
            link_dict[link.page.url] = link_dict.get(link.page.url) or []
            link_dict[link.page.url].append(link.html)

        with open(self.path, 'w') as file:
            file.write(json.dumps(link_dict, indent=2))
