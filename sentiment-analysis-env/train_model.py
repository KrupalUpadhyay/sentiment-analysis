import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df["Cleaned_Tweet"], df["Sentiment"]

def preprocess_data(X):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(X)
    return X, vectorizer

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    return model

if __name__ == "__main__":
    X, y = load_data("cleaned_tweets.csv")
    X, vectorizer = preprocess_data(X)
    model = train_model(X, y)
    joblib.dump(model, "sentiment_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print("Model and vectorizer saved")
