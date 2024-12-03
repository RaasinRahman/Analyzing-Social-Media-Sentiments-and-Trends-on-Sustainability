import tweepy

def get_api():
    # Replace with your API keys
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_TOKEN_SECRET = "your_access_token_secret"

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def fetch_tweets(hashtags, count=100):
    api = get_api()
    tweets_data = []
    for hashtag in hashtags:
        for tweet in tweepy.Cursor(api.search_tweets, q=f"#{hashtag}", lang="en").items(count):
            tweets_data.append({
                "text": tweet.text,
                "created_at": tweet.created_at.isoformat(),
                "user": tweet.user.screen_name,
                "likes": tweet.favorite_count,
                "retweets": tweet.retweet_count,
            })
    return tweets_data