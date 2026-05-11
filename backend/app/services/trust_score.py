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

    try:

        score = 75

        positive_signals = []

        risk_flags = []

        url = data.get(
            "url",
            ""
        )

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

        # HTTPS CHECK
        if url.startswith(
            "https://"
        ):

            score += 10

            positive_signals.append(
                "Uses HTTPS encryption"
            )

        else:

            score -= 20

            risk_flags.append(
                "Website does not use HTTPS"
            )

        # ABOUT PAGE
        if any(
            "about" in p.lower()
            for p in pages
        ):

            score += 5

            positive_signals.append(
                "About page detected"
            )

        # CONTACT PAGE
        if any(
            "contact" in p.lower()
            for p in pages
        ):

            score += 5

            positive_signals.append(
                "Contact page detected"
            )

        # CONTENT QUALITY
        content_length = len(content)

        if content_length > 5000:

            score += 5

            positive_signals.append(
                "Rich website content"
            )

        elif content_length < 500:

            score -= 10

            risk_flags.append(
                "Very limited content"
            )

        # METADATA QUALITY
        if len(description) > 50:

            score += 5

            positive_signals.append(
                "Detailed metadata found"
            )

        # STRUCTURED HEADINGS
        if len(headings) > 5:

            score += 5

            positive_signals.append(
                "Structured headings detected"
            )

        # SUSPICIOUS CONTENT
        detected_keywords = []

        for keyword in SUSPICIOUS_KEYWORDS:

            if keyword in content:

                detected_keywords.append(
                    keyword
                )

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

        # DOMAIN VALIDATION
        parsed = urlparse(url)

        domain = parsed.netloc

        if "." in domain and len(domain) > 5:

            score += 3

            positive_signals.append(
                "Valid domain structure"
            )

        # SCORE LIMIT
        score = max(
            0,
            min(score, 100)
        )

        # TRUST LEVEL
        if score >= 85:

            trust_level = "Very High"

        elif score >= 70:

            trust_level = "High"

        elif score >= 50:

            trust_level = "Medium"

        else:

            trust_level = "Low"

        result = {

            "trust_score": score,

            "trust_level": trust_level,

            "positive_signals":
            positive_signals,

            "risk_flags":
            risk_flags
        }

        print(
            "TRUST SCORE RESULT:",
            result
        )

        return result

    except Exception as e:

        print(
            "TRUST SCORE ERROR:",
            str(e)
        )

        return {

            "trust_score": 0,

            "trust_level": "Unknown",

            "positive_signals": [],

            "risk_flags": [
                str(e)
            ]
        }