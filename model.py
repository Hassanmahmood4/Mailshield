from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def build_vectorizer():
    return TfidfVectorizer(stop_words="english", max_features=5000)

def build_model():
    return MultinomialNB()