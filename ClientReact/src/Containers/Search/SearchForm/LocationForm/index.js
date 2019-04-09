import React from 'react'
import {DropDown} from '../../../../Presentational/Search'


class LocationForm extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        Country: 'United States',
        State: 'California',
        City: 'Irvine'
    };
    this.title = 'Search Location Details';
    this.data =
    [
            {id: 1, title: 'Country', content: [{value: 'United States'}, {value: 'Sweden'}]},
            {id: 2, title: 'State', content: [{value:'California'}, {value:'Texas'}]},
            {id: 3, title: 'City', content: [{value: 'Irvine'}, {value: 'Anaheim'}]}
    ];

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
            <DropDown title={this.title} options={this.data} handleChange={this.handleChange} handleSubmit={this.handleSubmit}/>
        )
    }
}

export default LocationForm;


