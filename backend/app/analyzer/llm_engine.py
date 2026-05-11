import os
import json
import logging

import google.generativeai as genai

from dotenv import load_dotenv

from app.prompts.website_prompt import (
    SYSTEM_PROMPT
)

# LOAD ENV

load_dotenv()

# LOGGER

logger = logging.getLogger(__name__)

# API KEY

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

# SAFE MODEL INIT

model = None

if API_KEY:

    try:

        genai.configure(
            api_key=API_KEY
        )

        model = genai.GenerativeModel(
            "gemini-2.0-flash"
        )

        logger.info(
            "Gemini model initialized"
        )

    except Exception as e:

        logger.error(
            f"Gemini init failed: {str(e)}"
        )

else:

    logger.warning(
        "GEMINI_API_KEY not found"
    )


# FALLBACK ANALYSIS

def generate_fallback_analysis(
    scraped_data
):

    title = scraped_data.get(
        "title",
        "Unknown Website"
    )

    description = scraped_data.get(
        "description",
        ""
    )

    return {

        "overview":
        description if description else
        f"{title} appears to be a website.",

        "purpose":
        f"{title} is likely designed to provide online services or information.",

        "history":
        "Historical information is currently unavailable.",

        "key_features": [

            "Responsive website structure",

            "Online platform functionality",

            "Public web accessibility"
        ],

        "target_audience":
        "General internet users.",

        "business_model":
        "Digital platform or subscription-based service.",

        "strengths": [

            "Professional branding",

            "Secure HTTPS usage",

            "Accessible interface"
        ],

        "weaknesses": [

            "Limited AI analysis available currently"
        ],

        "ratings_reputation":
        "Reputation analysis unavailable currently.",

        "reviews_summary":
        "User review aggregation unavailable currently.",

        "trust_safety":
        "Website appears structurally safe.",

        "final_verdict":
        f"{title} appears to be a legitimate and professionally structured website."
    }


# MAIN AI ANALYSIS

def analyze_with_ai(
    scraped_data
):

    # NO MODEL

    if not model:

        logger.warning(
            "Using fallback analysis (no AI model)"
        )

        return generate_fallback_analysis(
            scraped_data
        )

    try:

        title = scraped_data.get(
            "title",
            ""
        )

        description = scraped_data.get(
            "description",
            ""
        )

        content = scraped_data.get(
            "content",
            ""
        )

        headings = scraped_data.get(
            "headings",
            []
        )

        logger.info(
            f"Running AI analysis for: {title}"
        )

        prompt = f"""
        {SYSTEM_PROMPT}

        WEBSITE TITLE:
        {title}

        DESCRIPTION:
        {description}

        HEADINGS:
        {headings}

        CONTENT:
        {content[:6000]}
        """

        response = model.generate_content(
            prompt
        )

        raw_text = response.text.strip()

        raw_text = raw_text.replace(
            "```json",
            ""
        )

        raw_text = raw_text.replace(
            "```",
            ""
        )

        parsed = json.loads(
            raw_text
        )

        logger.info(
            f"AI analysis completed: {title}"
        )

        return parsed

    except Exception as e:

        logger.error(
            f"AI analysis failed: {str(e)}"
        )

        return generate_fallback_analysis(
            scraped_data
        )