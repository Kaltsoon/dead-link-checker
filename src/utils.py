from urllib.parse import urlparse, unquote
from pyquery import PyQuery
import httpx
from async_lru import alru_cache


def get_url_without_fragment(url: str):
    return url.split('#')[0]


def get_url_fragment(url: str):
    parts = url.split('#')

    return parts[1] if len(parts) > 1 else None


def html_has_fragment_target(html: str, fragment: str):
    query = PyQuery(html)
    normalized_id = unquote(fragment)

    selectors = [f'#{target},[href="#{target}"]' for target in [fragment, normalized_id]]
    selector = ','.join(selectors)

    return len(query(selector)) > 0


def get_base_url(url: str):
    uri = urlparse(url)

    return f'{uri.scheme}://{uri.netloc}'


@alru_cache(maxsize=200)
async def get_url_response(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, follow_redirects=True)

            return response
        except httpx.RequestError:
            return None


async def url_is_broken(url: str):
    normalized_url = get_url_without_fragment(url)

    response = await get_url_response(normalized_url)

    if response is None or response.status_code == 404 or response.status_code >= 500:
        return True

    fragment = get_url_fragment(url)

    if fragment is None or fragment.startswith('/'):
        return False

    return not html_has_fragment_target(response.text, fragment)
