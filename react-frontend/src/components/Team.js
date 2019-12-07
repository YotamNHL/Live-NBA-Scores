import React, { Component } from 'react'

class Team extends Component {

    render() {
        return (
            // <div className={this.props.winner ? 'team winner team--1' : 'team team--1'}>
            <div className="team team--1">
            <div className="team__details">
                <div className="team__details--logo">
                    <img src={this.props.imageSrc} alt="" />
                </div>
                <div className="team__details--name">
                    {this.props.name}
                </div>
            </div>
            <div className="team__total">
                {this.props.score}
            </div>
        </div>
        )
    }
}

export default Team;
