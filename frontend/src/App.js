import React, { useState, useEffect } from 'react';

const App = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/submissions');

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Network response was not ok: ${errorText}`);
        }

        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchData();
  }, []); // Empty dependency array means this effect runs once when the component mounts

  return (
    <div className="App">
      <h1>Welcome to /r/Music Maker</h1>
      <p>Turn your favorite /r/music posts into playlists!</p>

      {error && <p>Error: {error}</p>}

      {data.length > 0 ? (
        <div>
          <h2>All Submissions</h2>
          <ul>
            {data.map((submission, index) => (
                <li key={index}>
                  <a href={submission.url} target="_blank" rel="noopener noreferrer">
                    <strong>{submission.title}</strong>
                  </a>
                </li>
            ))}
          </ul>
        </div>
      ) : (
          <p>No submissions found.</p>
      )}
    </div>
  );
};

export default App;
