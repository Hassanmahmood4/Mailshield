import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

from utils import clean_text
from model import build_vectorizer, build_model

def main():
    # Load dataset (Kaggle SMS Spam Collection)
    df = pd.read_csv("data/spam.csv", encoding="latin-1")

    # Keep only required columns (some versions have extra unnamed columns)
    df = df[["v1", "v2"]]
    df = df.rename(columns={"v1": "label", "v2": "text"})

    # Convert labels to numeric
    df["label"] = df["label"].map({"spam": 1, "ham": 0})

    # Clean text
    df["clean_text"] = df["text"].astype(str).apply(clean_text)

    X = df["clean_text"]
    y = df["label"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Vectorize
    vectorizer = build_vectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train model
    model = build_model()
    model.fit(X_train_vec, y_train)

    # Evaluate
    y_pred = model.predict(X_test_vec)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Save artifacts
    joblib.dump(model, "spam_model.joblib")
    joblib.dump(vectorizer, "tfidf_vectorizer.joblib")
    print("\n✅ Model and vectorizer saved!")

if __name__ == "__main__":
    main()