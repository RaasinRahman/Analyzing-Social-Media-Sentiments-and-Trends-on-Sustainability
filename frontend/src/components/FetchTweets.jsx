import React, { useState } from "react";

const FetchTweets = ({ onFetch }) => {
  const [hashtags, setHashtags] = useState("");

  const fetchTweets = async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/fetch_tweets`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hashtags: hashtags.split(",") }),
      });

      const data = await response.json();
      console.log("Fetched Tweets:", data);

      onFetch(data, hashtags.split(",")); // Send fetched data and hashtags to App
    } catch (error) {
      console.error("Error fetching tweets:", error);
    }
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
    </div>
  );
};

export default FetchTweets;