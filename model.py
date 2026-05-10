import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("CEAS_08.csv")
print(data.columns)

# Show first rows
print(data.head())

# Email text column
X = data["body"]

# Label column
y = data["label"]

# Convert text into numbers
vectorizer = CountVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")

print("\n============================")
print(" PHISHING EMAIL DETECTOR ")
print("============================")

# User Input
# User Input
email = input("\nEnter Email Text: ")

email_data = vectorizer.transform([email])

# Phishing keywords
phishing_words = [
    "win",
    "winner",
    "claim",
    "click",
    "urgent",
    "bank",
    "password",
    "verify",
    "lottery",
    "prize"
]

# Check keywords
email_lower = email.lower()

keyword_detected = False

for word in phishing_words:
    if word in email_lower:
        keyword_detected = True
        break

# ML Prediction
prediction = model.predict(email_data)

# Final Result
if prediction[0] == 1 or keyword_detected:
    print("\nPrediction: Phishing Email")
    print("Threat Level: HIGH")
else:
    print("\nPrediction: Safe Email")
    print("Threat Level: LOW")