import React from 'react'
import {Location} from '../../../../Presentational/Search'


class LocationForm extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        Country: '',
        State: '',
        City: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(key) {
        return function (e) {
            var state = {};
            state[key] = e.target.value;
            this.setState(state);
        }.bind(this);
    }

    handleSubmit(event) {
        alert('Entered: ' + this.state.Country + ', ' + this.state.State + ', ' + this.state.City);
        event.preventDefault();
    }

    render() {
        return (
            <Location location={this.state} handleChange={this.handleChange} handleSubmit={this.handleSubmit}/>
        )
    }
}

export default LocationForm;


