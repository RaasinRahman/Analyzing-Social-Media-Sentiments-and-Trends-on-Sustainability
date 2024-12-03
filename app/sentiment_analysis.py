from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to analyze the sentiment of a list of tweets
def analyze_sentiments(tweets):
    analyzer = SentimentIntensityAnalyzer()
    results = []

    for tweet in tweets:
        text = tweet.get("text", "")
        score = analyzer.polarity_scores(text)
        results.append({
            "text": text,
            "sentiment": score,
            "created_at": tweet.get("created_at", "N/A"),  # Default to "N/A" if not provided
            "user": tweet.get("user", "Anonymous"),       # Default to "Anonymous" if not provided
        })

    return results