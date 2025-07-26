import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Load model and vectorizer
# model = joblib.load("logistic_model.pkl")
# vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Load model and vectorizer using full path
model = joblib.load(os.path.join(BASE_DIR, "logistic_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "tfidf_vectorizer.pkl"))

st.title("📧 Spam Detector with Logistic Regression")

user_input = st.text_area("Enter your message:", "")

if st.button("Predict"):
    vec_input = vectorizer.transform([user_input])
    prediction = model.predict(vec_input)[0]
    proba = model.predict_proba(vec_input)[0][1]

    label = "Spam" if prediction == 1 else "Not Spam"
    st.markdown(f"### 🔍 Prediction: **{label}**")
    st.markdown(f"Probability of Spam: `{proba:.2f}`")
