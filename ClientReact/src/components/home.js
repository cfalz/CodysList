import React from 'react'
import Item from './Item.js'

class Header extends React.Component {
    render () {
        return (
            <div>
                <h1> Home </h1>
                <ul className="header">
                    <li><a href="/"> Home </a></li>
                    <li><a href="/Listings"> Listings </a></li>
                </ul>
                <ul className="items">
                    <li> <Item name="item 1"/> </li> <br/>
                </ul>
            </div>
        );
    }
}

export default Header;