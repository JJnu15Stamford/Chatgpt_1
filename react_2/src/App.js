import React, { useState } from 'react';
import Card from './Components/Card';
import './Components/Card.css';

function App() {
  const [count, setCount] = useState(0); // React Hook to track button click count

  const handleButtonClick = () => {
    setCount(count + 1);
  };

  return (
    <div className="app">
      <h1>Welcome to My React App</h1>
      <button onClick={handleButtonClick}>Click me</button>
      <p>Button clicked {count} times</p>

      {/* Rendering the Card component and passing props */}
      <Card 
        title="Card Title" 
        description="This is a description of the card." 
        imageUrl="https://via.placeholder.com/150" 
      />
    </div>
  );
}

export default App;

