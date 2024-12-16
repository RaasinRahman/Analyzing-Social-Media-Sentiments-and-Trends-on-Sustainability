import tweepy
from app.mock_data import mock_tweets

def get_api():
    # Replace with your API keys
    API_KEY = ""
    API_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""


    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def fetch_tweets(hashtags, count=10):
    # Normalize hashtags: strip '#' and convert to lowercase
    normalized_hashtags = [tag.lstrip("#").lower() for tag in hashtags]

    filtered_tweets = []
    for tweet in mock_tweets:
        # Split tweet text into words and extract hashtags
        words = tweet["text"].split()
        tweet_hashtags = [word.lstrip("#").lower() for word in words if word.startswith("#")]

        # Match normalized hashtags with hashtags in the tweet
        if any(tag in tweet_hashtags for tag in normalized_hashtags):
            filtered_tweets.append(tweet)

    return filtered_tweets[:count]