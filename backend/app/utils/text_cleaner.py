import re

def clean_text(text: str) -> str:
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove weird characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text.strip()