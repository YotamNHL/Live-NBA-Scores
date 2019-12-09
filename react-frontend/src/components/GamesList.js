import React, { Component } from 'react'
import GameResult from './GameResult';
import backend from '../services/backend';

/* The Game list component. A simple list rerendering of all the game 'GameResult' component (the scoreboard). */
class GamesList extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            games: [],
            teamName: ""
        };
    }

    // An interval to update the game list every 90 seconds (the data base itself is
    // being updated at a rate of every 30 seconds).
    componentDidMount() {
        this.updateGames();
        console.log("Team name from super is:" + this.state.teamName)
        setInterval(this.updateGames, 1000 * 30);
    }

    updateGames = () => {
        backend.getLatestGames(this.state.teamName)
        .then(gamesResult => this.setState({ games: gamesResult }));
    }

    onChange = (event) => {
        const { name, value } = event.target;
        this.setState({ [name]: value });
        setTimeout(() => { 
            if (this.state.teamName==="") {
                this.updateGames();
                console.log("Team name now is: " + this.state.teamName);
            }
        }, 0);
      }
      
      onClick = (event) => {
        event.preventDefault();
        this.updateGames();
      }

    getGamesElements = (games) => {
        
        // Get all the games results as GameResult elements 
        const gamesToShow = games.map(game => {
            return <GameResult key={game.id} gameId={game.id} home={game.home} away={game.away} 
                               homeScore={game.home_score} awayScore={game.away_score}
                               homeImg={game.homeImg} awayImg={game.awayImg}/>;
        });
        
        return (
            <div>
                {gamesToShow}
            </div>
        )
    }

    render() {
        const { games } = this.state;
        const gamesLoaded = games.length > 0;
        
        // Checks if there are games to show, with a "Loading..." placeholder if not.
        return (
            <div>
                <input type="text" size="25" class="inputTextBig" id="team_input" name="teamName" onChange={this.onChange}/>
                <br/>
                <input type="submit" value="Filter Team" class="inputSubmit" onClick={this.onClick}/> 
                { gamesLoaded ? this.getGamesElements(games) : <div>Loading....</div> }
            </div>
        );
    }
}


export default GamesList;