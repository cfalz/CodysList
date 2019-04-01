import React from 'react'
import { Auction } from '../../AuctionBoard'

const AuctionList = ({ auctions }) =>
    <div>
        <h1> Auctions </h1>
        <div>
            {auctions.map(auction => <Auction name={auction.name}/>
            )}
        </div>
    </div>;

export default AuctionList



