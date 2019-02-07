import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: 'clicked'
    }
    this.handleClick = this.handleClick.bind(this)
  }

  handleClick(event) {
    event.preventDefault();
    if(this.state.clicked == 'clicked'){
      this.setState({
        clicked: "unclicked"
      })
    }
    if(this.state.clicked == 'unclicked'){
      this.setState({
        clicked: 'clicked'
      })
    }
  }
  render() {
    return (
      <div className={this.state.clicked}>
        <button onClick = {this.handleClick}> click here!</button>
      </div>
    );
  }
}

export default App;
