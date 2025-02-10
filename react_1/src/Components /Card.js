import React, { useState } from 'react';
// import App from './App.js';
import 'Card.css';


// Card component with useState hook
function Card({ title, description, imageUrl }) {
  // State hook for tracking the like/unlike status
  const [liked, setLiked] = useState(false);

  // Toggle the liked status when the button is clicked
  const handleLikeClick = () => {
    setLiked(!liked); // Toggle the "liked" state
  };

  return (
    <div className="card">
      <img src={imageUrl} alt={title} className="card-image" />
      <div className="card-content">
        <h2>{title}</h2>
        <p>{description}</p>
        <button onClick={handleLikeClick} className="like-button">
          {liked ? "Unlike" : "Like"} {/* Conditionally render the text based on "liked" state */}
        </button>
      </div>
    </div>
  );
}

export default Card;


