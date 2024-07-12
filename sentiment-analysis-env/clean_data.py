import pandas as pd
import re

def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs
    tweet = re.sub(r'@\w+', '', tweet)     # Remove mentions
    tweet = re.sub(r'#\w+', '', tweet)     # Remove hashtags
    tweet = re.sub(r'\d+', '', tweet)      # Remove numbers
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Remove punctuation
    tweet = tweet.lower()                  # Convert to lowercase
    return tweet

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file, encoding='latin1', header=None, usecols=[0, 5], names=["Sentiment", "Tweet"])
    df["Sentiment"] = df["Sentiment"].replace({0: "negative", 4: "positive"})
    df["Cleaned_Tweet"] = df["Tweet"].apply(clean_tweet)
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data("training.1600000.processed.noemoticon.csv", "cleaned_tweets.csv")
