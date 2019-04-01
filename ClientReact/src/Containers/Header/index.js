import React from 'react'

class Header extends React.Component {
    render() {
            return (
                <div className='header'>
                    <h1> Home </h1>
                    <ul>
                        <li><a href="/"> Home </a></li>
                        <li><a href="/Auctions"> Auctions </a></li>
                    </ul>
                 </div>
            );
    }
}

export default Header;
