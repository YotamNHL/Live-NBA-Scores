import React, { Component } from 'react'
import Team from './Team';
import './GameResult.css'

class GameResult extends Component {
    
    render() {
		const isHomeWinner = this.props.homeScore > this.props.awayScore;
        return (
			<div className="scoreboard">
				<div className="title">
					Teams
				</div>

                <div class="quaters">
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
