import React, { useState } from 'react';
import axios from 'axios';

const UserInput = () => {
  const handleClick = async () => {
    const text = prompt("Please enter your text:");
    if (text) {
      try {
        const response = await axios.post('http://localhost:4000/api/process-text', { text });
        console.log(response.data); // Handle the response from the backend
      } catch (error) {
        console.error(error);
      }
    }
  };

  return (
    <div>
    <button onClick={handleClick}>Click me</button>
    </div>
  );
};

export default UserInput;
