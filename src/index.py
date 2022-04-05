import os
from pathlib import Path
import click
from scraper import Scraper
from loggers.console_logger import ConsoleLogger
from reporters.file_reporter import FileReporter

dirname = os.path.dirname(__file__)

DATA_PATH = os.path.join(dirname, '..', 'data')


@click.command()
@click.option('--url', help='The URL of the page where the scraping starts')
@click.option('--max-depth', default=10, help='Maximum depth of pages to scrape')
@click.option(
    '--report-file',
    default='report.json',
    help='File where the report will be written in JSON format'
)
def scrape(url='', max_depth=10, report_file=None):
    logger = ConsoleLogger()

    report_path = Path(os.path.join(DATA_PATH, report_file)).resolve()

    scraper = Scraper(
        url=url,
        max_depth=max_depth,
        logger=logger
    )

    reporter = FileReporter(report_path, logger)

    logger.info(f'Starting the scraping at {url}...')

    reporter.produce_report(scraper)


if __name__ == '__main__':
    scrape()
