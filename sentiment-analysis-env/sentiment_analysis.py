import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score

if __name__ == "__main__":
    df = pd.read_csv('processed_tweets.csv')
    df['Sentiment'] = df['Processed_Text'].apply(lambda x: get_sentiment(x)['compound'])
    df.to_csv('sentiment_tweets.csv', index=False)
    print(df.head())
