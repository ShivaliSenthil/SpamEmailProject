# 📧 Spam Email Classification Web App

🔗 [Live Demo](https://shivali-spam-email-classification-webapp.streamlit.app/)

This is a simple and interactive web app built with **Streamlit** that classifies emails as **Spam** or **Not Spam** using a machine learning model.

---

## 🚀 Features

- 🔍 Classifies user-input email text as "Spam" or "Not Spam"
- 🤖 Uses a trained **Naive Bayes** or other ML classifier
- 🌐 Deployed on **Streamlit Cloud**
- 📦 Lightweight and easy to use

---

## 🧠 How it Works

1. **Text Preprocessing**: The input email is cleaned (lowercasing, stopwords removal, etc.)
2. **Vectorization**: The cleaned text is converted to numerical format using `TfidfVectorizer`.
3. **Prediction**: A trained model predicts whether the email is spam or not.

---

## 🛠️ Tech Stack

- 🐍 Python
- 🧠 Scikit-learn (for ML model)
- ✨ Streamlit (for the web interface)
- 🧹 NLTK or similar libraries (for text preprocessing)

---

## 📁 Project Structure

```plaintext
├── spam_classifier.pkl         # Trained ML model
├── vectorizer.pkl              # TfidfVectorizer
├── app.py                      # Streamlit app code
├── requirements.txt            # Required Python packages
└── README.md                   # This file
