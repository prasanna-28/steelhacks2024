import React from 'react';
import './App.css';
import logo from './logo.svg';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="http://127.0.0.1:5000/download/SteelHacks.pdf" 
          target="_blank"
          rel="noopener noreferrer"
        >
          Download PDF
        </a>
      </header>
    </div>
  );
}

export default App;