import joblib
from clean_data import clean_tweet

# Load the model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentiment(tweet):
    cleaned_tweet = clean_tweet(tweet)
    X = vectorizer.transform([cleaned_tweet])
    prediction = model.predict(X)
    return prediction[0]

if __name__ == "__main__":
    sample_tweets = [
        "I love using Python for data science!",
        "This is the worst day of my life.",
        "I'm so excited about the new project.",
        "I feel terrible today."
    ]

    for tweet in sample_tweets:
        sentiment = predict_sentiment(tweet)
        print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")
