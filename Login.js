import React, { useState, useEffect } from 'react';
import './App.css';

function LoginPage() {
    let [state,changeState]=useState()

  const [aadhaar, setAadhaar] = useState('');
  const [otp, setOtp] = useState('');
  const [isHuman, setIsHuman] = useState(false);
  
  // Mouse movement tracking
  const [mouseData, setMouseData] = useState([]);

  const trackMouseMovement = (e) => {
    setMouseData((prev) => [...prev, { x: e.clientX, y: e.clientY, time: Date.now() }]);
  };

  useEffect(() => {
    window.addEventListener('pointermove', trackMouseMovement);
    return () => {
      window.removeEventListener('pointermove', trackMouseMovement);
    };
  }, []);

  const handleLogin = async () => {
    // Send mouse data to the backend for analysis
    const response = await fetch('/api/analyze-mouse', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ mouseData }),
    });

    const result = await response.json();
    if (result.isHuman) {
      setIsHuman(true);
      // Proceed with OTP logic
    } else {
      // Bot detected, handle accordingly
      alert("Bot detected! Access denied.");
    }
  };

  return (
    <div className="login-container">
      <h2>Unique Identification Authority of India</h2>
      <div className="login-form">
        <input 
          type="text" 
          value={aadhaar} 
          onChange={(e) => setAadhaar(e.target.value)} 
          placeholder="Enter Aadhaar" 
        />
        <button onClick={handleLogin}>Send OTP</button>
        <input 
          type="text" 
          value={otp} 
          onChange={(e) => setOtp(e.target.value)} 
          placeholder="Enter OTP" 
          disabled={!isHuman}
        />
        <button disabled={!isHuman}>Login</button>
      </div>
    </div>
  );
}

export default LoginPage;
