# ⚰️ Dead Link Checker

[![Test](https://github.com/Kaltsoon/dead-link-checker/actions/workflows/test.yml/badge.svg)](https://github.com/Kaltsoon/dead-link-checker/actions/workflows/test.yml)

A dead-simple way (pun intended) to recursively look for broken links on a web page. Link is considered broken if its URL responds with an HTTP error status code or sends no response. Link with an [URI fragment](https://en.wikipedia.org/wiki/URI_fragment) is considered broken if there's no target for the fragment on the corresponding page.

## Requirements

Python version 3.9 or later.

## How to use?

With Docker:

1. Run the container by running `docker run --rm -v /path/to/data:/usr/src/app/data kaltsoon/dead-link-checker --url <url>` with the desired URL. Once the script is finished, it will write a report to the `/path/to/data/report.json` file which contains broken links per URL. Note that the script will only go through the internal links to avoid things getting out of hand. Run `docker run --rm kaltsoon/dead-link-checker --help` to see available options.

Without Docker:

1. Create a virtual environmennt by running `python3 -m venv env` and activate it by running `source env/bin/activate`.
2. Install dependencies inside the virtual environment by running `pip3 install -r requirements.txt`.
3. Inside the virtual environment run `python3 src/index.py --url <url>` with the desired URL. Once the script is finished, it will write a report to the `data/report.json` file which contains broken links per URL. Note that the script will only go through the internal links to avoid things getting out of hand. Run `python3 src/index.py --help` to see available options.
