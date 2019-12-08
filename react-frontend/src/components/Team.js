import React, { Component } from 'react'

/* The team component. 2 of these component are part of the GameResult component. */
class Team extends Component {

    render() {
        return (
            /* Different styling for the team who's leading (or the team who's won). */
            <div className={this.props.winner ? 'team winner team--1' : 'team team--1'}>
                <div className="team__details">
                    <div className="team__details--logo">
                        <img src={this.props.imageSrc} alt="" />
                    </div>
                    <div className="team__details--name">
                        {this.props.name}
                    </div>
                </div>
                <div class="team__score team__score--1"></div>
		        <div class="team__score team__score--2"></div>
		        <div class="team__score team__score--3"></div>
		        <div class="team__score team__score--4"></div>
                <div className="team__total">
                    {this.props.score}
                </div>
            </div>
        )
    }
}

export default Team;
