import os
import subprocess
import sys

def run_training():
    print("🔧 Training spam classifier...")
    subprocess.run([sys.executable, "train_spam_classifier.py"], check=True)

def main():
    if not os.path.exists("spam_model.joblib") or not os.path.exists("tfidf_vectorizer.joblib"):
        run_training()
    else:
        print("✅ Model already trained. Skipping training.")

    print("\n🖥️ To start the MailShield web app, run this command in your terminal:\n")
    print("   streamlit run app.py\n")
    print("🌐 Then open the link shown in the browser (usually http://localhost:8501)")

if __name__ == "__main__":
    main()