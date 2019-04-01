import React, {Component} from 'react'
import {Auction} from '../../Presentational/AuctionBoard'

class AuctionBoard extends Component {
    constructor() {
        super();
        this.state = { auctions: [{ name: 'Car', imageUrl: 'images/skyline.jpg', }, { name: 'Truck', imageUrl: 'images/truck.jpg', }] };
  }

  componentDidMount() {
    //TODO::Need to fetch auctions from backend here
    const auctionArray = [ { name: 'Car', imageUrl: 'images/skyline.jpg', }, { name: 'Truck', imageUrl: 'images/truck.jpg', } ]

    this.setState( {auctionArray} )
  }

  render() {

    return (
        <div>
            <div>
                <h1> Auctions </h1>
                <div>
                    {this.state.auctions.map((auction) => <Auction auction={auction}/> )}
                </div>
            </div>
        </div>
    )
  }
}

export default AuctionBoard;

