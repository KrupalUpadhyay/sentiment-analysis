import tweepy
import pandas as pd

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Set up Tweepy API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch tweets
def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
    tweet_list = [[tweet.created_at, tweet.text] for tweet in tweets]
    return pd.DataFrame(tweet_list, columns=["Datetime", "Text"])

# Example usage
if __name__ == "__main__":
    df = fetch_tweets("AI", 100)
    df.to_csv('tweets.csv', index=False)
    print(df.head())
