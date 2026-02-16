📧 Mailsheild — Email/SMS Spam Detection with Machine Learning

Mailsheild is a simple and effective spam detection system built using Machine Learning (NLP) and a Streamlit web interface.
It classifies messages as Spam or Not Spam using a trained text classification model — all running locally on your machine.

<img width="758" height="462" alt="image" src="https://github.com/user-attachments/assets/82421a8d-43a5-49c1-8477-0f9414059b5a" />
<img width="759" height="477" alt="image" src="https://github.com/user-attachments/assets/149bda56-c01d-4e5d-8992-15567b1ca025" />


✨ Features
	•	🧠 ML-based spam classification (Naive Bayes + TF-IDF)
	•	📝 Text preprocessing (cleaning & normalization)
	•	⚡ Fast predictions
	•	🌐 Interactive web interface using Streamlit
	•	🔒 Runs locally (no external APIs required)
	•	📊 High accuracy on standard spam datasets


🧰 Tech Stack
	•	Python 3.9+
	•	scikit-learn – machine learning
	•	pandas – data processing
	•	Streamlit – web UI
	•	joblib – model persistence
	•	NLP (TF-IDF) – feature extraction


📁 Project Structure

Mailsheild/
├── data/
│   └── spam.csv              # Dataset (Kaggle SMS Spam Collection)
├── app.py                    # Streamlit web app (UI)
├── main.py                   # Entry point (setup helper)
├── train_spam_classifier.py  # Model training script
├── predict.py                # CLI prediction script
├── model.py                  # Model + vectorizer builders
├── utils.py                  # Text preprocessing helpers
├── requirements.txt          # Dependencies
└── README.md




🚀 Getting Started

1️⃣ Clone the Repository

git clone https://github.com/Hassanmahmood4/Mailsheild.git
cd Mailsheild




2️⃣ Set Up Virtual Environment (Optional but Recommended)

python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows

Install dependencies:

pip install -r requirements.txt



3️⃣ Add Dataset

Download the SMS Spam Collection Dataset from Kaggle:

👉 https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

Place the file here:

Mailsheild/data/spam.csv

The dataset should contain columns v1 (label: spam/ham) and v2 (message).


4️⃣ Train the Model

python train_spam_classifier.py

This will generate:

spam_model.joblib
tfidf_vectorizer.joblib



5️⃣ Run the Web App (Streamlit)

streamlit run app.py

Open the link shown in the terminal (usually http://localhost:8501) and start testing messages 🎉



▶️ Optional: Quick Start with main.py

You can run:

python main.py

This will:
	•	Check if the trained model exists
	•	Guide you to train the model if needed
	•	Show you how to start the Streamlit UI



🧪 Example Test Messages

Spam:

🎉 CONGRATULATIONS! You’ve won a FREE iPhone. Click now to claim!

Not Spam:

Hey, are we meeting at 6 pm today?


🧠 How It Works (High Level)
	1.	Input text is cleaned and normalized
	2.	Text is converted to numeric features using TF-IDF
	3.	A trained Naive Bayes classifier predicts Spam vs Not Spam
	4.	Result is displayed in the Streamlit UI


📈 Model Performance
	•	Accuracy typically 97–99% on the Kaggle SMS Spam dataset
	•	Metrics used: Accuracy, Precision, Recall, F1-score



🛣️ Future Improvements
	•	🔢 Show prediction confidence (probability)
	•	📁 Batch CSV upload for bulk predictions
	•	🧪 Try other models (Logistic Regression, SVM)
	•	☁️ Deploy on Streamlit Community Cloud
	•	📊 Add evaluation dashboard



🙌 Acknowledgements
	•	Kaggle – SMS Spam Collection Dataset
	•	scikit-learn – ML library
	•	Streamlit – Web UI framework

