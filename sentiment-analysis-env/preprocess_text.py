import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(tokens)

if __name__ == "__main__":
    df = pd.read_csv('cleaned_tweets.csv')
    df['Processed_Text'] = df['Cleaned_Text'].apply(preprocess_text)
    df.to_csv('processed_tweets.csv', index=False)
    print(df.head())
