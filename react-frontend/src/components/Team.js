import React, { Component } from 'react'

class Team extends Component {
    
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div class={this.props.winner ? 'team winner team--1' : 'team team--1'}>
            <div class="team__details">
                <div class="team__details--logo">
                    <img src={this.props.imageSrc} alt="" />
                </div>
                <div class="team__details--name">
                    {this.props.name}
                </div>
            </div>
            <div class="team__total">
                {this.props.score}
            </div>
        </div>
        )
    }
}

export default Team;
