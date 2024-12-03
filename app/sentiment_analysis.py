from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiments(tweets):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    for tweet in tweets:
        score = analyzer.polarity_scores(tweet["text"])
        results.append({
            "text": tweet["text"],
            "sentiment": score,
            "created_at": tweet["created_at"],
            "user": tweet["user"]
        })
    return results