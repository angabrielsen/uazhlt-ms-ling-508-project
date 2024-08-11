import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  const [submissions, setSubmissions] = useState([]);
  const [url, setUrl] = useState('');
  const [error, setError] = useState(null);

  const fetchSubmissions = async () => {
    try {
      const response = await fetch('http://localhost:5000/submissions');
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Network response was not ok: ${errorText}`);
      }
      const result = await response.json();
      setSubmissions(result); // Update the state with the result
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
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

      await response.json();
      setUrl('');
      fetchSubmissions();

    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="HomePage">
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

      {error && <p>Error: {error}</p>}

      <ul>
        {submissions.map((submission) => (
          <li key={submission.id}>
            <Link to={`/comments/${submission.submission_id}`}>
              <strong>{submission.title}</strong>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
