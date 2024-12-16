# backend/app/sentiment_utils.py

import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiments(tweets):
    df = pd.DataFrame({'tweet': tweets})
    
    # Analyze Sentiment
    def analyze_sentiment(tweet):
        scores = sia.polarity_scores(tweet)
        return scores['compound'], scores['pos'], scores['neu'], scores['neg']

    df[['compound', 'positive', 'neutral', 'negative']] = df['tweet'].apply(
        lambda x: pd.Series(analyze_sentiment(x))
    )

    # Classify Sentiments
    def classify_sentiment(compound):
        if compound > 0.05:
            return 'Positive'
        elif compound < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    df['sentiment'] = df['compound'].apply(classify_sentiment)
    return df.to_dict(orient='records')