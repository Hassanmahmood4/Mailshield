import streamlit as st
import joblib
from utils import clean_text

@st.cache_resource
def load_artifacts():
    model = joblib.load("spam_model.joblib")
    vectorizer = joblib.load("tfidf_vectorizer.joblib")
    return model, vectorizer

def main():
    st.set_page_config(page_title="MailShield", page_icon="📧", layout="centered")

    st.title("📧 MailShield")
    st.write("Protect your inbox. Detect whether an email is **Spam** or **Not Spam** using AI.")

    email_text = st.text_area("Paste your email text here:", height=200)

    if st.button("Detect Spam 🚀"):
        if not email_text.strip():
            st.warning("Please enter some email text.")
        else:
            with st.spinner("Analyzing email..."):
                model, vectorizer = load_artifacts()
                clean = clean_text(email_text)
                vec = vectorizer.transform([clean])
                pred = model.predict(vec)[0]

            if pred == 1:
                st.error("🚨 This email is classified as **SPAM**")
            else:
                st.success("✅ This email is **NOT SPAM**")

if __name__ == "__main__":
    main()