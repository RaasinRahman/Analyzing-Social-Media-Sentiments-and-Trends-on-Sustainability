from flask import Blueprint, request, jsonify
from app.twitter_utils import fetch_tweets
from textblob import TextBlob
import re

main = Blueprint("main", __name__)

def clean_text(text):
    """
    Clean text by removing hashtags, URLs, punctuation, and extra spaces.
    """
    text = re.sub(r"#\w+", "", text)  # Remove hashtags
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    return text.strip()

def analyze_textblob_sentiment(text):
    """
    Analyze sentiment using TextBlob.
    If sentiment is neutral, assign 'Positive' for specific domain keywords.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # Custom logic for neutral results
    if polarity == 0:
        keywords = ["sustainability", "eco-friendly", "renewable", "green"]
        if any(word in text.lower() for word in keywords):
            return {"polarity": 0.2, "classification": "Positive"}

    if polarity > 0:
        return {"polarity": polarity, "classification": "Positive"}
    elif polarity < 0:
        return {"polarity": polarity, "classification": "Negative"}
    else:
        return {"polarity": polarity, "classification": "Neutral"}

@main.route("/fetch_tweets", methods=["POST"])
def fetch_tweets_route():
    hashtags = request.json.get("hashtags", [])
    tweets = fetch_tweets(hashtags)

    for tweet in tweets:
        cleaned_text = clean_text(tweet.get("text", ""))
        sentiment = analyze_textblob_sentiment(cleaned_text)
        tweet['sentiment'] = sentiment

    return jsonify(tweets)