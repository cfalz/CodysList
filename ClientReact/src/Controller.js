import React, {Component} from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import {AuctionBoard, Home, Header} from './Containers'

class Controller extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    <div className="header">
                        <Header />
                    </div>
                    <div>
                        <Route exact={true} path='/' render={ () => ( <div> <Home/> </div> )}/>
                        <Route exact={true} path='/Auctions' render={ () => ( <div> <AuctionBoard/> </div> )}/>
                    </div>
                </div>
            </BrowserRouter>
        ); //End Return
    } //End Render
} //End Controller

export default Controller;
