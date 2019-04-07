import React, {Component} from 'react'
import {LocationForm} from './SearchForm'


class Search extends Component {
  render() {
    return (
        <div>
            <div>
                <h1> Search For Auction </h1>
                <body>
                    <div>
                        { < LocationForm /> }
                    </div>
                </body>
            </div>
        </div>
    )
  }
}

export default Search;
