import streamlit as st
from real_time_predict import predict_sentiment

st.title("Sentiment Analysis")

st.subheader("Enter Tweet")
tweet = st.text_input("Tweet")

if st.button("Predict Sentiment"):
    sentiment = predict_sentiment(tweet)
    st.write(f"Sentiment: {sentiment}")

st.subheader("Sample Predictions")
sample_tweets = [
    "I love using Python for data science!",
    "This is the worst day of my life.",
    "I'm so excited about the new project.",
    "I feel terrible today."
]

for tweet in sample_tweets:
    sentiment = predict_sentiment(tweet)
    st.write(f"Tweet: {tweet}\nSentiment: {sentiment}\n")
