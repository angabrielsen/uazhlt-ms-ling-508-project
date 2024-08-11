import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const CommentsPage = () => {
  const { id } = useParams();
  const [comments, setComments] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchComments = async () => {
      try {
        const response = await fetch(`http://localhost:5000/get_comments/${id}`);
        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Network response was not ok: ${errorText}`);
        }
        const result = await response.json();
        setComments(result.comments); // Adjust based on actual response structure
      } catch (err) {
        setError(err.message);
      }
    };

    fetchComments();
  }, [id]);

  return (
    <div className="CommentsPage">
      <h1>Comments</h1>
      {error && <p>Error: {error}</p>}
      <ul>
        {comments.map((comment, index) => (
          <li key={index}>{comment}</li>
        ))}
      </ul>
    </div>
  );
};

export default CommentsPage;
