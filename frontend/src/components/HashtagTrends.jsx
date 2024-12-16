import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend
);

const HashtagTrends = ({ tweets, selectedHashtag }) => {
  const [trendData, setTrendData] = useState(null);
  const [sentimentChartData, setSentimentChartData] = useState(null);

  useEffect(() => {
    if (selectedHashtag && tweets.length > 0) {
      calculateTrend(selectedHashtag);
      calculateSentiments(selectedHashtag);
    }
  }, [tweets, selectedHashtag]);

  const calculateTrend = (hashtag) => {
    const normalizedHashtag = hashtag.toLowerCase().trim();

    const filteredTweets = tweets.filter((tweet) =>
      tweet.text
        .toLowerCase()
        .split(" ")
        .some((word) => word.replace("#", "") === normalizedHashtag)
    );

    const trends = filteredTweets.reduce((acc, tweet) => {
      const date = new Date(tweet.created_at).toISOString().split("T")[0];
      acc[date] = acc[date] || { tweets: 0, likes: 0, retweets: 0 };
      acc[date].tweets += 1;
      acc[date].likes += tweet.likes || 0;
      acc[date].retweets += tweet.retweets || 0;
      return acc;
    }, {});

    const dates = Object.keys(trends).sort();
    const data = {
      dates,
      tweets: dates.map((date) => trends[date].tweets),
      likes: dates.map((date) => trends[date].likes),
      retweets: dates.map((date) => trends[date].retweets),
    };

    setTrendData(data);
  };

  const calculateSentiments = (hashtag) => {
    const normalizedHashtag = hashtag.toLowerCase().trim();

    const filteredTweets = tweets.filter((tweet) =>
      tweet.text
        .toLowerCase()
        .split(" ")
        .some((word) => word.replace("#", "") === normalizedHashtag)
    );

    const sentiments = filteredTweets.reduce((acc, tweet) => {
      const date = new Date(tweet.created_at).toISOString().split("T")[0];
      acc[date] = acc[date] || { positive: 0, neutral: 0, negative: 0 };

      if (tweet.sentiment) {
        const polarity = tweet.sentiment.polarity;
      
        if (polarity > 0) {
          acc[date].positive += 1;
        } else if (polarity < 0) {
          acc[date].negative += 1;
        } else {
          acc[date].neutral += 1;
        }
      }

      return acc;
    }, {});

    const dates = Object.keys(sentiments).sort();
    const data = {
      dates,
      positive: dates.map((date) => sentiments[date].positive),
      neutral: dates.map((date) => sentiments[date].neutral),
      negative: dates.map((date) => sentiments[date].negative),
    };

    setSentimentChartData(data);
  };

  return (
    <div>
      <h2>Hashtag Trends</h2>
      {tweets.length > 0 && (
        <ul>
          {tweets.map((tweet, index) => (
            <li key={index}>
              <strong>{tweet.user}</strong>: {tweet.text}{" "}
              <em>({new Date(tweet.created_at).toLocaleDateString()})</em>
            </li>
          ))}
        </ul>
      )}
      {trendData && (
        <div>
          <h3>Trend Chart for #{selectedHashtag}</h3>
          <Line
            data={{
              labels: trendData.dates,
              datasets: [
                {
                  label: "Tweets",
                  data: trendData.tweets,
                  borderColor: "rgba(75, 192, 192, 1)",
                  borderWidth: 2,
                  fill: false,
                },
                {
                  label: "Likes",
                  data: trendData.likes,
                  borderColor: "rgba(255, 99, 132, 1)",
                  borderWidth: 2,
                  fill: false,
                },
                {
                  label: "Retweets",
                  data: trendData.retweets,
                  borderColor: "rgba(54, 162, 235, 1)",
                  borderWidth: 2,
                  fill: false,
                },
              ],
            }}
            options={{
              responsive: true,
              scales: {
                x: {
                  title: { display: true, text: "Date" },
                },
                y: {
                  title: { display: true, text: "Count" },
                  beginAtZero: true,
                },
              },
            }}
          />
        </div>
      )}
      {sentimentChartData && (
        <div>
          <h3>Sentiment Chart for #{selectedHashtag}</h3>
          <Line
            data={{
              labels: sentimentChartData.dates,
              datasets: [
                {
                  label: "Positive Sentiments",
                  data: sentimentChartData.positive,
                  borderColor: "rgba(75, 192, 192, 1)",
                  borderWidth: 2,
                  fill: false,
                },
                {
                  label: "Neutral Sentiments",
                  data: sentimentChartData.neutral,
                  borderColor: "rgba(201, 203, 207, 1)",
                  borderWidth: 2,
                  fill: false,
                },
                {
                  label: "Negative Sentiments",
                  data: sentimentChartData.negative,
                  borderColor: "rgba(255, 99, 132, 1)",
                  borderWidth: 2,
                  fill: false,
                },
              ],
            }}
            options={{
              responsive: true,
              scales: {
                x: {
                  title: { display: true, text: "Date" },
                },
                y: {
                  title: { display: true, text: "Count" },
                  beginAtZero: true,
                },
              },
            }}
          />
        </div>
      )}
    </div>
  );
};

export default HashtagTrends;