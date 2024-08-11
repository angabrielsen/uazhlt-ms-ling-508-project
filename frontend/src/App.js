import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage'; // Make sure this matches the filename
import CommentsPage from './CommentsPage'; // Make sure this matches the filename

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/comments/:id" element={<CommentsPage />} />
    </Routes>
  </Router>
);

export default App;
