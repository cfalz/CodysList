import React from 'react'

class Header extends React.Component {
    render() {
            return (
                <div className='header'>
                    <ul>
                        <li><a href="/"> Auctioneer </a></li>
                        <li><a href="/Auctions"> Auctions </a></li>
                        <li><a href="/Search"> Search </a></li>
                        <li><a href="/AddAuction"> Add Auction </a></li>
                    </ul>
                 </div>
            );
    }
}

export default Header;
