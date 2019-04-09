import React, {Component} from 'react'
import {LocationForm, AuctionCategoryForm, ContactInformationForm} from './SearchForm'


class Search extends Component {
    render() {
        return (
        <div>
            <h1> Search For Auction </h1>
            <body>
                <div>
                    { < LocationForm /> }
                    { < AuctionCategoryForm /> }
                    { < ContactInformationForm /> }
                </div>
            </body>
        </div>
        )
    }
}

export default Search;
