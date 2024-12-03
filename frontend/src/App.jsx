import React from "react";
import FetchTweets from "./components/FetchTweets";
import AnalyzeSentiments from "./components/AnalyzeSentiments";

function App() {
  return (
    <div>
      <h1>Social Media Sentiment Analysis</h1>
      <FetchTweets />
      <AnalyzeSentiments />
    </div>
  );
}

export default App;