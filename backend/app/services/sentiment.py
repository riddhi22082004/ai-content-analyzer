from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    try:
        if not text.strip():
            return "No content"

        # limit text
        text = text[:1000]

        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        # convert to labels
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"

    except Exception as e:
        return f"Sentiment Error: {str(e)}"