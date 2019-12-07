import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';



class App extends Component {
  state= {
    games : [
       { '_id': 0, home: '76ers', away: 'suns', home_score: 78, away_score: 99}
    ]
  }


  render() {

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Live Scores</h1>
        </header>
        <div className="game_window">a</div>
      </div>
    );
  }
}

export default App;
