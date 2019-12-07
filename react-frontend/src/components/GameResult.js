import React, { Component } from 'react'
import Team from './Team';
import './GameResult.css'

class GameResult extends Component {
    
    constructor(props) {
        super(props);
    }
    
    render() {
		const isHomeWinner = this.props.homeScore > this.props.awayScore;
        return (
			<div class="scoreboard">
				<div class="title">
					Teams
				</div>

				<div class="total">
					Score
				</div>

				<Team winner={isHomeWinner} name={this.props.home} score={this.props.homeScore} imageSrc={this.props.homeImg || 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/124740/bears.png'}/>
				<Team winner={!isHomeWinner} name={this.props.away} score={this.props.awayScore} imageSrc={this.props.awayImg || 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/124740/cremes.png'}/>
				
			</div>
		)
    }
}

export default GameResult;
