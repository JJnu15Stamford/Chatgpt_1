import React, { useState } from 'react';
import Card from './Components/Card'; // Import Card component
import './App.css'; // Main app CSS

function App() {
  const [count, setCount] = useState(0);

  const handleButtonClick = () => {
    setCount(count + 1); // Increment the count on button click
  };

  return (
    <div className="app">
      <h1>Welcome to My React App</h1>
      <button onClick={handleButtonClick}>Click me</button>
      <p>Button clicked {count} times</p>

      {/* Passing props to the Card component */}
      <Card 
        title="Card Title" 
        description="This is a description of the card."
        imageUrl="https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt4a4af7e6facea579/6668df6ceca9a600983250ac/beautiful-flowers-hero.jpg?q=70&width=3840&auto=webp" 
      />
    </div>
  );
}

export default App;
