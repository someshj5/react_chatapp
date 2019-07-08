import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import Book from "./Component/chatapp/index";
import { registration } from './Component/chatapp/registration';
import { login } from './Component/chatapp/login';

class App extends Component {

  getuser =(e) => {
    e.preventDefault();
    const user = e.target.elements.username.value;
    console.log(user); 
  }
  render() {
    return (
      <Router>

        <Route path="/" exact component={Book} />
        <Route path="/registration" exact component={registration} />
        <Route path="/login" exact component={login} />

    </Router>

    );
  }
}



//function App() {
//  return (
//    <div className="App">
//      <header className="App-header">
//        <img src={logo} className="App-logo" alt="logo" />
//        <p>
//          Edit <code>src/App.js</code> and save to reload.
//        </p>
//        <a
//          className="App-link"
//          href="https://reactjs.org"
//          target="_blank"
//          rel="noopener noreferrer"
//        >
//          Learn React
//        </a>
//      </header>
//    </div>
//  );
//}

export default App;
