import React from 'react'

const Auction = ({auction}) =>
    <div className='auctionItem'>
        <div className='auctionName'>
            <h2> {auction.name} </h2>
        </div>
        <div className='auctionItemImageUrl'>
            <img src={auction.imageUrl} alt={auction.name} />
        </div>
    </div>;

export default Auction