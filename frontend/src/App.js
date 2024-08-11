import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './HomePage';
import Comments from './CommentsPage';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/comments/:id" element={<Comments />} />
    </Routes>
  </Router>
);

export default App;
