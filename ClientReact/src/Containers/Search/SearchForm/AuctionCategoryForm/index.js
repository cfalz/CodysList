import React from 'react'
import {DropDown} from '../../../../Presentational/Search'


class AuctionCategoryForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            category_one: 'Automotive',
            category_two: 'Car',
            category_three: 'Coupe'
        };
        this.title = 'Auction Category';
        this.data =
        [
                {id: 1, title: 'Category One', content: [{value: 'Automotive'}, {value: 'Electronics'}]},
                {id: 2, title: 'Category Two', content: [{value:'Car'}, {value:'Computer'}]},
                {id: 3, title: 'Category Three', content: [{value: 'Coupe'}, {value: 'Laptop'}]}
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


    render() { return ( <DropDown title={this.title} options={this.data} handleChange={this.handleChange} handleSubmit={this.handleSubmit} /> ) }
}

export default AuctionCategoryForm;