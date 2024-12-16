import React, { useState } from "react";
import FetchTweets from "./components/FetchTweets";
import HashtagTrends from "./components/HashtagTrends";
import AnalyzeSentiments from "./components/AnalyzeSentiments";

function App() {
  const [tweets, setTweets] = useState([]);
  const [activeHashtag, setActiveHashtag] = useState("");

  const handleFetchTweets = (data, hashtags) => {
    setTweets(data); // Set tweets state
    if (hashtags.length > 0) {
      setActiveHashtag(hashtags[0]); // Set the first hashtag as active
    }
  };

  return (
    <div>
      <h1>Social Media Sentiment Analysis</h1>
      <FetchTweets onFetch={handleFetchTweets} />
      <HashtagTrends tweets={tweets} selectedHashtag={activeHashtag} />
    
    </div>
  );
}

export default App;