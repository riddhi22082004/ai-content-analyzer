from urllib.parse import urlparse


def analyze_trust(url, metadata):

    score = 50

    positive_signals = []

    risk_flags = []

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    description = metadata.get(
        "description",
        ""
    )

    content = metadata.get(
        "content",
        ""
    )

    combined = (
        description + " " + content
    ).lower()

    # HTTPS

    if parsed.scheme == "https":

        score += 15

        positive_signals.append(
            "Uses HTTPS encryption"
        )

    else:

        score -= 20

        risk_flags.append(
            "Website is not secured with HTTPS"
        )

    # VALID DOMAIN

    if "." in domain:

        score += 5

        positive_signals.append(
            "Valid domain structure"
        )

    # DESCRIPTION QUALITY

    if len(description) > 60:

        score += 10

        positive_signals.append(
            "Detailed website metadata found"
        )

    else:

        score -= 5

        risk_flags.append(
            "Weak or limited metadata"
        )

    # CONTENT QUALITY

    content_length = len(content)

    if content_length > 3000:

        score += 15

        positive_signals.append(
            "Substantial website content detected"
        )

    elif content_length > 1000:

        score += 8

        positive_signals.append(
            "Moderate website content detected"
        )

    else:

        score -= 10

        risk_flags.append(
            "Very limited website content"
        )

    # TRUSTED DOMAINS

    trusted_domains = [
        "github.com",
        "google.com",
        "microsoft.com",
        "openai.com",
        "netflix.com",
        "amazon.com",
        "apple.com"
    ]

    if any(td in domain for td in trusted_domains):

        score += 20

        positive_signals.append(
            "Recognized globally trusted platform"
        )

    # SUSPICIOUS WORDS

    suspicious_words = [
        "free money",
        "win cash",
        "hack",
        "crack",
        "casino",
        "adult",
        "betting",
        "cheat"
    ]

    found_suspicious = False

    for word in suspicious_words:

        if word in combined:

            found_suspicious = True

            break

    if found_suspicious:

        score -= 25

        risk_flags.append(
            "Suspicious or risky keywords detected"
        )

    # DOMAIN LENGTH

    if len(domain) > 35:

        score -= 10

        risk_flags.append(
            "Unusually long domain name"
        )

    # FINAL LIMITS

    score = max(
        5,
        min(score, 100)
    )

    # TRUST LEVEL

    if score >= 85:

        trust_level = "High"

    elif score >= 60:

        trust_level = "Medium"

    else:

        trust_level = "Low"

    return {
        "trust_score": score,
        "trust_level": trust_level,
        "positive_signals": positive_signals,
        "risk_flags": risk_flags
    }