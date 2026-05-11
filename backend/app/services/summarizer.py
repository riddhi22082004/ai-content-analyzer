from transformers import pipeline

summarizer_pipeline = None  # global variable

def get_summarizer():
    global summarizer_pipeline

    if summarizer_pipeline is None:
        summarizer_pipeline = pipeline(
            task="summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    return summarizer_pipeline


def summarize_text(text: str) -> str:
    try:
        if not text.strip():
            return "No content to summarize"

        text = text[:1200]

        summarizer = get_summarizer()

        result = summarizer(
            text,
            max_length=120,
            min_length=30,
            do_sample=False
        )

        return result[0]["summary_text"]

    except Exception as e:
        return f"Summarization Error: {str(e)}"