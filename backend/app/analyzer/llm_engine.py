import os
import json

import google.generativeai as genai

from dotenv import load_dotenv

from app.prompts.website_prompt import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:

    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel(
        "gemini-2.0-flash"
    )

else:

    model = None


def generate_fallback_analysis(scraped_data):

    title = scraped_data.get(
        "title",
        "Unknown Website"
    )

    description = scraped_data.get(
        "description",
        ""
    )

    content = scraped_data.get(
        "content",
        ""
    )

    combined = (
        f"{title} {description} {content}"
    ).lower()

    # PURPOSE DETECTION

    if any(word in combined for word in [
        "developer",
        "repository",
        "code",
        "software"
    ]):

        purpose = (
            "This platform is focused on software "
            "development and collaboration services."
        )

    elif any(word in combined for word in [
        "movie",
        "series",
        "watch",
        "stream"
    ]):

        purpose = (
            "This platform provides online streaming "
            "and entertainment services."
        )

    elif any(word in combined for word in [
        "shopping",
        "buy",
        "cart",
        "product"
    ]):

        purpose = (
            "This platform is used for online "
            "shopping and e-commerce."
        )

    elif any(word in combined for word in [
        "ai",
        "artificial intelligence",
        "machine learning"
    ]):

        purpose = (
            "This platform provides AI-powered "
            "technology or research services."
        )

    else:

        purpose = (
            "This website provides digital online services."
        )

    # HISTORY DETECTION

    if "github" in combined:

        history = (
            "GitHub was launched in 2008 and became "
            "one of the world's leading code hosting "
            "and collaboration platforms."
        )

    elif "netflix" in combined:

        history = (
            "Netflix started as a DVD rental service "
            "before evolving into a global streaming platform."
        )

    elif "openai" in combined:

        history = (
            "OpenAI was founded in 2015 with the mission "
            "of developing safe and beneficial AI systems."
        )

    elif "amazon" in combined:

        history = (
            "Amazon evolved from an online bookstore "
            "into one of the world's largest e-commerce companies."
        )

    else:

        history = (
            "Detailed historical information "
            "could not be identified automatically."
        )

    # KEY FEATURES DETECTION

    features = []

    if "login" in combined:

        features.append(
            "User authentication system"
        )

    if "search" in combined:

        features.append(
            "Search functionality"
        )

    if "repository" in combined:

        features.append(
            "Code repository hosting"
        )

    if "stream" in combined or "video" in combined:

        features.append(
            "Streaming capabilities"
        )

    if "ai" in combined:

        features.append(
            "AI-powered services"
        )

    if "cloud" in combined:

        features.append(
            "Cloud-based infrastructure"
        )

    if len(features) == 0:

        features = [
            "Public website access",
            "Digital platform"
        ]

    # TARGET AUDIENCE

    if "developer" in combined:

        audience = (
            "Software developers and technology teams"
        )

    elif "movie" in combined or "stream" in combined:

        audience = (
            "Entertainment and streaming audiences"
        )

    else:

        audience = "General internet users"

    # BUSINESS MODEL

    if "subscription" in combined:

        business_model = (
            "Subscription-based digital platform"
        )

    elif "shopping" in combined:

        business_model = (
            "E-commerce business model"
        )

    else:

        business_model = (
            "Digital service platform"
        )

    # STRENGTHS

    strengths = [
        "Professional website structure",
        "Accessible public platform"
    ]

    if "https" in combined:

        strengths.append(
            "Secure HTTPS support"
        )

    # WEAKNESSES

    weaknesses = []

    if len(description) < 50:

        weaknesses.append(
            "Limited descriptive metadata"
        )

    weaknesses.append(
        "Public review data may be limited"
    )

    # REPUTATION

    if "github" in combined:

        reputation = (
            "Widely trusted by developers and enterprises worldwide."
        )

    elif "netflix" in combined:

        reputation = (
            "Globally recognized entertainment platform."
        )

    elif "openai" in combined:

        reputation = (
            "Well-known AI research and technology organization."
        )

    else:

        reputation = (
            "Public reputation information is limited."
        )

    # REVIEWS

    if "github" in combined:

        reviews = (
            "Popular among developers for version control "
            "and collaboration tools."
        )

    elif "netflix" in combined:

        reviews = (
            "Users generally praise its streaming quality "
            "and content library."
        )

    elif "openai" in combined:

        reviews = (
            "Recognized for advanced AI tools and research innovation."
        )

    else:

        reviews = (
            "Detailed public review information unavailable."
        )

    # TRUST

    trust = (
        "Website appears professionally maintained "
        "and structurally safe."
    )

    # FINAL VERDICT

    verdict = (
        f"{title} appears to be a legitimate "
        "and functional online platform."
    )

    return {
        "overview": description,
        "purpose": purpose,
        "history": history,
        "key_features": features,
        "target_audience": audience,
        "business_model": business_model,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "ratings_reputation": reputation,
        "reviews_summary": reviews,
        "trust_safety": trust,
        "final_verdict": verdict
    }


def analyze_with_ai(scraped_data):

    if not model:

        return generate_fallback_analysis(
            scraped_data
        )

    try:

        prompt = f"""
{SYSTEM_PROMPT}

Website Data:
{json.dumps(scraped_data, indent=2)}

Return ONLY valid JSON.
"""

        response = model.generate_content(
            prompt
        )

        cleaned = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        parsed = json.loads(cleaned)

        return parsed

    except Exception as e:

        print("Gemini Error:", e)

        return generate_fallback_analysis(
            scraped_data
        )



def analyze_with_ai(scraped_data):

    if not model:

        return generate_fallback_analysis(
            scraped_data
        )

    try:

        important_data = {
            "title": scraped_data.get("title"),
            "description": scraped_data.get("description"),
            "content": scraped_data.get("content", "")[:12000]
        }

        prompt = f"""
{SYSTEM_PROMPT}

Website Data:
{json.dumps(important_data, indent=2)}
"""

        response = model.generate_content(
            prompt
        )

        raw_text = response.text.strip()

        cleaned = (
            raw_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        parsed = json.loads(cleaned)

        return parsed

    except Exception as e:

        print("GEMINI ERROR:", e)

        return generate_fallback_analysis(
            scraped_data
        )