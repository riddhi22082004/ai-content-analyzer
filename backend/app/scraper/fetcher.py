import asyncio
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/122 Safari/537.36"
    )
}


IMPORTANT_KEYWORDS = [
    "about",
    "company",
    "contact",
    "pricing",
    "features",
    "services",
    "products",
    "solutions",
    "faq",
    "security",
    "privacy"
]


async def fetch_html(session, url):

    try:

        async with session.get(
            url,
            headers=HEADERS,
            timeout=20
        ) as response:

            if response.status != 200:
                return ""

            return await response.text()

    except Exception:
        return ""


def extract_metadata(soup):

    title = ""

    if soup.title and soup.title.string:
        title = soup.title.string.strip()

    description = ""

    meta_desc = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if meta_desc:
        description = meta_desc.get(
            "content",
            ""
        ).strip()

    return title, description


def extract_headings(soup):

    headings = []

    for tag in soup.find_all(
        ["h1", "h2", "h3"]
    ):

        text = tag.get_text(
            " ",
            strip=True
        )

        if text and len(text) > 3:
            headings.append(text)

    return headings[:50]


def extract_content(soup):

    paragraphs = []

    for p in soup.find_all("p"):

        text = p.get_text(
            " ",
            strip=True
        )

        if len(text) > 50:
            paragraphs.append(text)

    return "\n".join(paragraphs[:50])


def parse_page(url, html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    title, description = extract_metadata(soup)

    headings = extract_headings(soup)

    content = extract_content(soup)

    return {
        "url": url,
        "title": title,
        "description": description,
        "headings": headings,
        "content": content
    }


async def discover_links(session, base_url):

    html = await fetch_html(
        session,
        base_url
    )

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    links = set()

    domain = urlparse(base_url).netloc

    for tag in soup.find_all(
        "a",
        href=True
    ):

        href = tag["href"]

        absolute = urljoin(
            base_url,
            href
        )

        parsed = urlparse(absolute)

        if parsed.netloc != domain:
            continue

        lower = absolute.lower()

        for keyword in IMPORTANT_KEYWORDS:

            if keyword in lower:
                links.add(absolute)

    return list(links)[:10]


async def crawl_page(session, url):

    html = await fetch_html(
        session,
        url
    )

    if not html:
        return None

    return parse_page(
        url,
        html
    )


async def async_fetch_website(url):

    async with aiohttp.ClientSession() as session:

        homepage_html = await fetch_html(
            session,
            url
        )

        if not homepage_html:

            return {
                "error": "Unable to fetch website"
            }

        homepage_data = parse_page(
            url,
            homepage_html
        )

        internal_links = await discover_links(
            session,
            url
        )

        tasks = [
            crawl_page(session, link)
            for link in internal_links
        ]

        pages = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        valid_pages = []

        for page in pages:

            if isinstance(page, dict):
                valid_pages.append(page)

        combined_content = homepage_data["content"]

        combined_headings = homepage_data["headings"]

        for page in valid_pages:

            combined_content += (
                "\n\n" + page["content"]
            )

            combined_headings.extend(
                page["headings"]
            )

        return {
            "title": homepage_data["title"],
            "description": homepage_data["description"],
            "content": combined_content[:30000],
            "headings": combined_headings[:100],
            "pages_crawled": [
                homepage_data["url"]
            ] + [
                p["url"]
                for p in valid_pages
            ]
        }


def fetch_website(url):

    return asyncio.run(
        async_fetch_website(url)
    )