import React, { useState } from 'react';

const App = () => {
  const [url, setUrl] = useState('');
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/get_comments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Network response was not ok: ${errorText}`);
      }

      const result = await response.json();
      setData(result);
      setError(null);
    } catch (err) {
      setError(err.message);
      setData(null);
    }
  };

  return (
    <div className="App">
      <h1>Welcome to /r/Music Maker</h1>
      <p>Turn your favorite /r/music posts into playlists!</p>

      {/* Simple Form */}
      <form onSubmit={handleSubmit}>
        <label htmlFor="url">Enter URL:</label>
        <input
          type="text"
          id="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter URL here"
          required
        />
        <button type="submit">Submit</button>
      </form>

      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
      {error && <p>Error: {error}</p>}
    </div>
  );
};

export default App;
