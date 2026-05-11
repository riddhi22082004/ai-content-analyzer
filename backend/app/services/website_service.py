from app.scraper.fetcher import fetch_website

from app.utils.trust_score import (
    calculate_trust_score
)

from app.services.orchestrator import (
    AIOrchestrator
)


def process_website(url):

    # STEP 1 — SCRAPE WEBSITE
    scraped_data = fetch_website(url)

    if scraped_data.get("error"):

        return {
            "success": False,
            "error": scraped_data["error"]
        }

    # STEP 2 — AI ANALYSIS
    orchestrator = AIOrchestrator()

    analysis = orchestrator.generate(
        scraped_data
    )

    # STEP 3 — TRUST ANALYSIS
    trust_analysis = calculate_trust_score({

        "url": url,

        "description":
        scraped_data.get(
            "description",
            ""
        ),

        "content":
        scraped_data.get(
            "content",
            ""
        ),

        "headings":
        scraped_data.get(
            "headings",
            []
        ),

        "pages_crawled":
        scraped_data.get(
            "pages_crawled",
            []
        )
    })

    # DEBUG
    print("AI ANALYSIS:", analysis)

    print(
        "TRUST ANALYSIS:",
        trust_analysis
    )

    print("TRUST ANALYSIS VALUE:")
    print(trust_analysis)

    # STEP 4 — FINAL RESPONSE
    return {

        "success": True,

        "url": url,

        "metadata": {

            "title":
            scraped_data.get(
                "title",
                ""
            ),

            "description":
            scraped_data.get(
                "description",
                ""
            )
        },

        "analysis": analysis,

        "trust_analysis":
        trust_analysis,

        "pages_crawled":
        scraped_data.get(
            "pages_crawled",
            []
        )
    }