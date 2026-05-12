from bs4 import BeautifulSoup

from newspaper import Article


def parse_website(html, url):

    title = ""
    description = ""
    content = ""

    try:

        # TRY NEWSPAPER

        article = Article(url)

        article.download()

        article.parse()

        title = article.title or ""

        content = article.text or ""

    except Exception:

        pass

    # FALLBACK TO BEAUTIFULSOUP

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # TITLE

    if not title and soup.title:

        title = soup.title.text.strip()

    # META DESCRIPTION

    meta = soup.find(
        "meta",
        attrs={
            "name": "description"
        }
    )

    if meta:

        description = meta.get(
            "content",
            ""
        )

    # PAGE TEXT

    if not content:

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        content = " ".join(
            text.split()
        )

    # LIMIT SIZE

    content = content[:15000]

    return {
        "title": title,
        "description": description,
        "content": content
    }