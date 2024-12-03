import React, { useState } from "react";

const FetchTweets = () => {
  const [hashtags, setHashtags] = useState("");
  const [tweets, setTweets] = useState([]);

  const fetchTweets = async () => {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/fetch_tweets`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ hashtags: hashtags.split(",") }),
    });
    const data = await response.json();
    setTweets(data);
  };

  return (
    <div>
      <h2>Fetch Tweets</h2>
      <input
        type="text"
        value={hashtags}
        onChange={(e) => setHashtags(e.target.value)}
        placeholder="Enter hashtags (comma-separated)"
      />
      <button onClick={fetchTweets}>Fetch</button>
      <ul>
        {tweets.map((tweet, index) => (
          <li key={index}>{tweet.text}</li>
        ))}
      </ul>
    </div>
  );
};

export default FetchTweets;