from bs4 import BeautifulSoup


def parse_website(html):

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    title = ""

    if soup.title:

        title = soup.title.text.strip()

    description = ""

    meta = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if meta:

        description = meta.get(
            "content",
            ""
        )

    headings = [
        h.text.strip()
        for h in soup.find_all(["h1", "h2", "h3"])
    ]

    paragraphs = [
        p.text.strip()
        for p in soup.find_all("p")
    ]

    content = " ".join(paragraphs)

    return {
        "title": title,
        "description": description,
        "headings": headings[:20],
        "content": content[:10000]
    }