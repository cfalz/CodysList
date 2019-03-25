import React, {Component} from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import NavbarLight from './components/home.js'

class Controller extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    {
                        <Route exact={true} path='/' render={ () => ( <div> <NavbarLight/> </div> )}/>
                    }
                </div>
            </BrowserRouter>
        ); //End Return
    } //End Render
} //End Controller

export default Controller;
