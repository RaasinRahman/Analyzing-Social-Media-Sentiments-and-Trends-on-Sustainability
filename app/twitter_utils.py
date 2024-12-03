import tweepy
from app.mock_data import mock_tweets

def get_api():
   
    API_KEY = ""
    API_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""


    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def fetch_tweets(hashtags, count=10):
    # Filter mock tweets by hashtags
    filtered_tweets = []
    for tweet in mock_tweets:
        if any(f"#{hashtag}" in tweet["text"] for hashtag in hashtags):
            filtered_tweets.append(tweet)
    return filtered_tweets[:count]  # Limit to 'count' tweets
