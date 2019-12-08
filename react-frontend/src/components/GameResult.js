import React, { Component } from 'react'
import Team from './Team';
import './GameResult.css'

/* The scoreboard component (which also consists of 2 'Team' component) one for every game session. */
class GameResult extends Component {
    
    render() {
		// This boolean will help us determine the necessary styling for each team in the component. 
		const isHomeWinner = parseInt(this.props.homeScore) > parseInt(this.props.awayScore);
		
		// With this veriable we'll add a feature in which
		// by press of the scoreboard it will open the game's page on ESPN
		const gameview = "https://www.espn.com/nba/game?gameId=" + this.props.gameId
        return (
			<a href={gameview} target="_blank">
			<div className="scoreboard">
				<div className="title">
					Teams
				</div>

                <div class="spacer">
	            </div>

				<div className="total">
					Score
				</div>

				<Team winner={isHomeWinner} name={this.props.home} score={this.props.homeScore} imageSrc={this.props.homeImg}/>
				<Team winner={!isHomeWinner} name={this.props.away} score={this.props.awayScore} imageSrc={this.props.awayImg}/>
			</div>
			</a>
		)
    }
}

export default GameResult;
