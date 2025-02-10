import React from 'react';
import './Card.css'; // Importing card-specific CSS

function Card({ title, description, imageUrl }) {
  return (
    <div className="card">
      <img src={imageUrl} alt={title} className="card-image" />
      <h2>{title}</h2>
      <p>{description}</p>
    </div>
  );
}

export default Card; // Exporting the Card component to use in other files
