import React, { Component } from 'react'
import GameResult from './GameResult';
import backend from '../services/backend';

class GamesList extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            games: []
        };
    }

    componentDidMount() {
        this.updateGames();
        setInterval(this.updateGames, 1000 * 20);
    }

    updateGames = () => {
        backend.getLatestGames()
        .then(gamesResult => this.setState({ games: gamesResult }))
    }

    getGamesElements = (games) => {
        
        // Get all the games results as GameResult elements 
        const gamesToShow = games.map(game => {
            return <GameResult home={game.home} away={game.away} 
                               homeScore={game.home_score} awayScore={game.away_score}/>;
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
        
        // check if there are games to show
        return gamesLoaded ? this.getGamesElements(games) : <div>Loading...</div>
    }
}


export default GamesList;