from flask import Blueprint, request, jsonify
from app.twitter_utils import fetch_tweets
from app.sentiment_analysis import analyze_sentiments
from app.models.database import get_mongo_collection

main = Blueprint("main", __name__)

@main.route("/fetch_tweets", methods=["POST"])
def fetch_tweets_route():
    hashtags = request.json.get("hashtags", [])
    tweets = fetch_tweets(hashtags)
    return jsonify(tweets)

@main.route("/analyze_sentiments", methods=["POST"])
def analyze_sentiments_route():
    tweets = request.json.get("tweets", [])
    sentiments = analyze_sentiments(tweets)
    return jsonify(sentiments)

@main.route("/save_data", methods=["POST"])
def save_data():
    data = request.json
    collection = get_mongo_collection()
    collection.insert_one(data)
    return jsonify({"status": "success"})