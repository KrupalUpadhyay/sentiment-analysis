import pandas as pd
import re

def clean_tweet(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

if __name__ == "__main__":
    df = pd.read_csv('tweets.csv')
    df['Cleaned_Text'] = df['Text'].apply(clean_tweet)
    df.to_csv('cleaned_tweets.csv', index=False)
    print(df.head())
