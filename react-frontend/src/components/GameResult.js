import React, { Component } from 'react'
import Team from './Team';
import './GameResult.css'

/* The scoreboard component (which also consists of 2 'Team' component) one for every game session. */
class GameResult extends Component {
    
    render() {
		/* This boolean will help us determine the necessary styling for each team in the component. */
		const isHomeWinner = parseInt(this.props.homeScore) > parseInt(this.props.awayScore);
        return (
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
		)
    }
}

export default GameResult;
