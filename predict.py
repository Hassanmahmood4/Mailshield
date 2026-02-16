import joblib
from utils import clean_text

def load_artifacts():
    model = joblib.load("spam_model.joblib")
    vectorizer = joblib.load("tfidf_vectorizer.joblib")
    return model, vectorizer

def predict_email(text: str):
    model, vectorizer = load_artifacts()
    text_clean = clean_text(text)
    vec = vectorizer.transform([text_clean])
    pred = model.predict(vec)[0]
    return "SPAM" if pred == 1 else "NOT SPAM"

if __name__ == "__main__":
    print("📧 Email Spam Detector")
    email = input("Enter email text: ")
    result = predict_email(email)
    print("Prediction:", result)