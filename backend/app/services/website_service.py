from app.scraper.fetcher import fetch_website
from app.scraper.parser import parse_website

from app.analyzer.llm_engine import analyze_with_ai
from app.analyzer.trust_engine import analyze_trust


SUPPORTED_BLOCKED_DOMAINS = [
    "amazon.",
    "flipkart.",
    "myntra.",
    "facebook.",
    "instagram.",
    "whatsapp."
]


def process_website(url):

    try:

        lowered = url.lower()

        for blocked in SUPPORTED_BLOCKED_DOMAINS:

            if blocked in lowered:

                return {
                    "success": False,
                    "error": (
                        "This website blocks automated scraping "
                        "or requires authentication."
                    )
                }

        # FETCH WEBSITE
        html = fetch_website(url)

        if not html:

            return {
                "success": False,
                "error": "Failed to fetch website content."
            }

        # PARSE WEBSITE
        parsed_data = parse_website(html)

        if not parsed_data:

            return {
                "success": False,
                "error": "Failed to parse website."
            }

        # AI ANALYSIS
        ai_analysis = analyze_with_ai(
            parsed_data
        )

        # TRUST ANALYSIS
        trust_analysis = analyze_trust(
            url,
            parsed_data
        )

        return {

            "success": True,

            "url": url,

            "metadata": {

                "title":
                parsed_data.get(
                    "title",
                    ""
                ),

                "description":
                parsed_data.get(
                    "description",
                    ""
                )
            },

            "analysis":
            ai_analysis,

            "trust_analysis":
            trust_analysis,

            "pages_crawled": [url]
        }

    except Exception as e:

        return {

            "success": False,

            "error":
            str(e)
        }