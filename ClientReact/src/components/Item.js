import React from 'react'

class Item extends React.Component {
    render () {
        return (
            <div class='item'>
                {this.props.name}
             </div>
        );
    }
}

export default Item;
