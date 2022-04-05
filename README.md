# ⚰️ Dead Link Checker

[![Test](https://github.com/Kaltsoon/dead-link-checker/actions/workflows/test.yml/badge.svg)](https://github.com/Kaltsoon/dead-link-checker/actions/workflows/test.yml)

A dead-simple way (pun intended) to recursively look for broken links on a web page. Link is considered broken if its URL responds with an HTTP error status code or sends no response. Link with an [URI fragment](https://en.wikipedia.org/wiki/URI_fragment) is considered broken if there's no target for the fragment on the corresponding page.

## Requirements

[Poetry](https://python-poetry.org/) and Python version 3.9 or later.

## How to use?

1. Install dependencies by running `poetry install`.
2. Run `poetry run python3 src/index.py --url <url>` with the desired URL. Once the script is finished, it will write a report to the `data/report.json` file which contains broken links per URL. Note that the script will only go through the internal links to avoid things getting out of hand. Run `poetry run python3 src/index.py --help` to see available options.
