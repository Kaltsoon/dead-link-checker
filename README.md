# ⚰️ Dead Link Checker

A dead simple way (pun intended) to recursively look for dead links on a web page. Link is considered dead if its URL responds with an HTTP error status code (4xx or 5xx) or sends no response.

## Requirements

[Poetry](https://python-poetry.org/) and Python version 3.9 or later.

## How to use?

1. Install dependencies by running `poetry install`.
2. Run `poetry run python3 src/index.py --url <url>` with the desired URL. Once the script is finished, it will write a report to the `data/report.json` file which contains dead links per URL. Note that the script will only go through the internal links to avoid things getting out of hand. Run `poetry run python3 src/index.py --help` to see available options.
