import React, { useState, useEffect } from 'react';

const App = () => {
  const [url, setUrl] = useState('');
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [submissions, setSubmissions] = useState([]);

  useEffect(() => {
    const fetchSubmissions = async () => {
      try {
        const response = await fetch('http://localhost:5000/submissions');

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Network response was not ok: ${errorText}`);
        }

        const result = await response.json();
        setSubmissions(result);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchSubmissions();
  }, []);

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

      const submissionsResponse = await fetch('http://localhost:5000/submissions');
      if (submissionsResponse.ok) {
        const submissionsResult = await submissionsResponse.json();
        setSubmissions(submissionsResult);
      }

    } catch (err) {
      setError(err.message);
      setData(null);
    }
  };

  return (
    <div className="App">
      <h1>Welcome to /r/Music Maker</h1>
      <p>Turn your favorite /r/music posts into playlists!</p>

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

      {data && (
        <div>
          <h2>Title: {data.title}</h2>
          <h3>Comments:</h3>
          <ul>
            {data.comments.map((comment, index) => (
              <li key={index}>{comment}</li>
            ))}
          </ul>
        </div>
      )}
      {error && <p>Error: {error}</p>}

      <div>
        <h2>All Submissions</h2>
        <ul>
          {submissions.map((submission, index) => (
            <li key={index}>
              <a href={submission.url} target="_blank" rel="noopener noreferrer">
                <strong>{submission.title}</strong>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default App;
