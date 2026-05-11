import re

# simple keyword-based scoring
FAKE_KEYWORDS = [
    "shocking", "breaking", "you won't believe",
    "miracle", "secret", "exposed", "fake", "hoax"
]

TRUSTED_SOURCES = [
    "wikipedia.org",
    "bbc.com",
    "nytimes.com",
    "reuters.com"
]

def calculate_credibility(url: str, text: str) -> int:
    score = 50  # base score

    # ✅ Check trusted source
    if any(source in url for source in TRUSTED_SOURCES):
        score += 30

    # ❌ Check fake keywords
    text_lower = text.lower()
    for word in FAKE_KEYWORDS:
        if word in text_lower:
            score -= 3
    # check excessive CAPS (clickbait)
    if text.isupper():
        score -= 10

    # ✅ Content length check
    if len(text) > 2000:
        score += 10
    else:
        score -= 10

    # Normalize
    score = max(0, min(100, score))

    return score