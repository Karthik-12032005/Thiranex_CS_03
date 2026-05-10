import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load Dataset
data = pd.read_csv("emails.csv")

# Columns
X = data["body"]
y = data["label"]

# Train Model
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

# UI
st.title("Phishing Email Detector")

email = st.text_area("Enter Email Text")

if st.button("Analyze"):

    email_data = vectorizer.transform([email])

    prediction = model.predict(email_data)

    phishing_words = [
    "win",
    "won",
    "winner",
    "claim",
    "click",
    "urgent",
    "bank",
    "password",
    "verify",
    "lottery",
    "prize",
    "free",
    "offer",
    "money",
    "cash",
    "gift"
]

    keyword_detected = any(word in email.lower() for word in phishing_words)

    if prediction[0] == 1 or keyword_detected:
        st.error("Phishing Email Detected")
        st.write("Threat Level: HIGH")
    else:
        st.success("Safe Email")
        st.write("Threat Level: LOW")