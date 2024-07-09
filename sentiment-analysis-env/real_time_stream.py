import tweepy
from tweepy.streaming import StreamListener
from fetch_tweets import clean_tweet, preprocess_text, get_sentiment

class MyStreamListener(StreamListener):
    def on_status(self, status):
        text = clean_tweet(status.text)
        processed_text = preprocess_text(text)
        sentiment = get_sentiment(processed_text)['compound']
        print(f"Tweet: {status.text}\nSentiment: {sentiment}\n")

    def on_error(self, status_code):
        if status_code == 420:
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['AI'], is_async=True)
