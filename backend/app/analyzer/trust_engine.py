from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "guaranteed money",
    "quick rich",
    "100% profit",
    "free cash",
    "instant earnings",
    "double your money",
    "risk free investment"
]


def calculate_trust_score(data: dict):

    score = 60

    positive_signals = []

    risk_flags = []

    url = data.get("url", "")

    description = data.get(
        "description",
        ""
    ).lower()

    content = data.get(
        "content",
        ""
    ).lower()

    pages = data.get(
        "pages_crawled",
        []
    )

    headings = data.get(
        "headings",
        []
    )

    # HTTPS
    if url.startswith("https://"):

        score += 10

        positive_signals.append(
            "Uses HTTPS encryption"
        )

    else:

        score -= 15

        risk_flags.append(
            "Website does not use HTTPS"
        )

    # ABOUT PAGE
    if any(
        "about" in p.lower()
        for p in pages
    ):

        score += 8

        positive_signals.append(
            "About page detected"
        )

    # CONTACT PAGE
    if any(
        "contact" in p.lower()
        for p in pages
    ):

        score += 8

        positive_signals.append(
            "Contact page detected"
        )

    # CONTENT QUALITY
    content_length = len(content)

    if content_length > 5000:

        score += 10

        positive_signals.append(
            "Rich website content"
        )

    elif content_length > 2000:

        score += 5

        positive_signals.append(
            "Moderate content availability"
        )

    else:

        score -= 5

        risk_flags.append(
            "Limited textual content"
        )

    # METADATA QUALITY
    if len(description) > 80:

        score += 5

        positive_signals.append(
            "Detailed metadata description"
        )

    elif len(description) < 20:

        score -= 5

        risk_flags.append(
            "Weak metadata description"
        )

    # STRUCTURED HEADINGS
    if len(headings) > 5:

        score += 5

        positive_signals.append(
            "Structured page headings detected"
        )

    # SUSPICIOUS KEYWORDS
    detected_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in content:
            detected_keywords.append(keyword)

    if detected_keywords:

        penalty = min(
            len(detected_keywords) * 10,
            30
        )

        score -= penalty

        risk_flags.append(
            f"Suspicious phrases detected: "
            f"{', '.join(detected_keywords)}"
        )

    # DOMAIN STRUCTURE
    parsed = urlparse(url)

    domain = parsed.netloc

    if "." in domain and len(domain) > 5:

        score += 4

        positive_signals.append(
            "Structured domain detected"
        )

    # NORMALIZE
    score = max(0, min(score, 100))

    # TRUST LEVEL
    if score >= 85:
        trust_level = "Very High"

    elif score >= 70:
        trust_level = "High"

    elif score >= 50:
        trust_level = "Medium"

    else:
        trust_level = "Low"

    return {

        "trust_score": score,

        "trust_level": trust_level,

        "positive_signals": positive_signals,

        "risk_flags": risk_flags
    }