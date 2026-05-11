def build_prompt(data: dict) -> str:
    return f"""
You are an advanced website intelligence analyzer.

Analyze the following website data carefully.

TITLE:
{data.get('title', '')}

DESCRIPTION:
{data.get('description', '')}

CONTENT:
{data.get('content', '')}

IMPORTANT:
Return ONLY valid JSON.

JSON FORMAT:

{{
    "overview": "Detailed website summary",
    "history": "Website/company history if available",
    "purpose": "Industry and problem solved",
    "key_features": [
        "feature 1",
        "feature 2"
    ],
    "ratings_reputation": "Ratings/reputation analysis",
    "reviews_summary": "Summary of user opinions",
    "trust_safety": "Trust and risk analysis",
    "final_verdict": "Balanced conclusion"
}}

RULES:
- Do not add markdown
- Do not add explanation outside JSON
- Always return valid JSON
"""