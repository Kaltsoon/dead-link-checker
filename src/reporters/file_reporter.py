import json


class FileReporter:
    def __init__(self, path):
        self.path = path

    def produce_report(self, scraper):
        broken_links = scraper.get_broken_links()

        link_dict = {}

        for link in broken_links:
            link_dict[link.page.url] = link_dict.get(link.page.url) or []
            link_dict[link.page.url].append(link.html)

        file = open(self.path, 'w')
        file.write(json.dumps(link_dict, indent=2))
        file.close()
