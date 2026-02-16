import re
import string

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\d+", "", text)  # remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # normalize spaces
    return text