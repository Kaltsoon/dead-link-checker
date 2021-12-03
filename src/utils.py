import requests
from functools import lru_cache
from urllib.parse import urlparse
from pyquery import PyQuery
from urllib.parse import unquote


def get_url_without_fragment(url):
    return url.split('#')[0]


def get_url_fragment(url):
    parts = url.split('#')

    return parts[1] if len(parts) > 1 else None


def html_has_fragment_target(html, fragment):
    query = PyQuery(html)
    normalized_id = unquote(fragment)

    return len(query(f'#{normalized_id},[href="#{normalized_id}"]')) > 0


def get_base_url(url):
    uri = urlparse(url)

    return f'{uri.scheme}://{uri.netloc}'


@lru_cache(maxsize=200)
def get_url_response(url):
    try:
        return requests.get(url, timeout=10)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None


def url_is_broken(url):
    normalized_url = get_url_without_fragment(url)

    response = get_url_response(normalized_url)

    if response is None or response.status_code != requests.codes.ok:
        return True

    fragment = get_url_fragment(url)

    if fragment is None or fragment.startswith('/'):
        return False

    return not html_has_fragment_target(response.text, fragment)
