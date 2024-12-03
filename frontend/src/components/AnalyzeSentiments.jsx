import React, { useState } from "react";

const AnalyzeSentiments = () => {
  const [tweets, setTweets] = useState([]);
  const [sentiments, setSentiments] = useState([]);

  const analyze = async () => {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/analyze_sentiments`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ tweets }),
    });
    const data = await response.json();
    setSentiments(data);
  };

  return (
    <div>
      <h2>Analyze Sentiments</h2>
      <textarea
        rows="5"
        value={tweets.map((tweet) => tweet.text).join("\n")}
        onChange={(e) =>
          setTweets(e.target.value.split("\n").map((text) => ({ text })))
        }
        placeholder="Enter tweets (one per line)"
      />
      <button onClick={analyze}>Analyze</button>
      <ul>
        {sentiments.map((sentiment, index) => (
          <li key={index}>
            <strong>{sentiment.text}</strong>: {JSON.stringify(sentiment.sentiment)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AnalyzeSentiments;