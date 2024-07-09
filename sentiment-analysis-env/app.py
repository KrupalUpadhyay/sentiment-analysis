import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title('Real-time Sentiment Analysis')

# Load data
df = pd.read_csv('sentiment_tweets.csv')

# Line chart
st.line_chart(df['Sentiment'])

# Histogram
fig, ax = plt.subplots()
sns.histplot(df['Sentiment'], kde=True, ax=ax)
st.pyplot(fig)
