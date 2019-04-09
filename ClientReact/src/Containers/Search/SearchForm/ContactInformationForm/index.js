import React from 'react'

class ContactInformationForm extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        Name: '',
        Number: '',
    };
    this.title = 'My Contact Information';
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

    }

    handleChange(key) {
        return function (e) {
            var state = {};
            state[key] = e.target.value;
            this.setState(state);
        }.bind(this);
    }

    handleSubmit(event) {
        alert('Entered: ' + this.state.Name + ', ' + this.state.Number)
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <h2> Contact Information </h2>
                <label>
                  Name: <br/>
                  <input type="text" value={this.state.Name} onChange={this.handleChange('Name')} />
                  <br/>
                  Number: <br/>
                  <input type="text" value={this.state.Number} onChange={this.handleChange('Number')} />
                  <br/>
                </label>
                <input type="submit" value="Submit" />
            </form>
        )
    }
}

export default ContactInformationForm;


