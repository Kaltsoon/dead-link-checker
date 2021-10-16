import requests
from functools import lru_cache
from urllib.parse import urlparse


def get_url_without_fragment(url):
    return url.split('#')[0]


def get_base_url(url):
    uri = urlparse(url)

    return f'{uri.scheme}://{uri.netloc}'


@lru_cache(maxsize=200)
def cached_url_is_broken(url):
    try:
        respose = requests.get(url, timeout=10)

        return respose.status_code != requests.codes.ok
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return True


def url_is_broken(url):
    normalized_url = get_url_without_fragment(url)

    return cached_url_is_broken(normalized_url)
