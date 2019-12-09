import React, { Component } from 'react';
import GamesList from './components/GamesList';
import logo from './logo.svg';
import './App.css';

class App extends Component {

  render() {


    return (
    

      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <div className="team_name_input">
          </div>
          <h1 className="App-title"></h1>
        </header>
        <div className="games-list">
          <GamesList/>
        </div>
      </div>
    );
  }
}

export default App;
