import React, { Component, Fragment } from 'react';
import { homedir } from 'os';
import Home from './components/Home'
import Head from './components/header'
import AuthorList from './components/authorList'
import './App.css'

import axios from "axios";


// const list = [
//   {
//     'id': 1,
//     'title': '1st Item',
//     'description': 'Description here.'
//   },
//   {
//     'id': 2,
//     'title': '2nd Item',
//     'description': 'Another description here.'
//   },
//   {
//     'id': 3,
//     'title': '3rd Item',
//     'description': 'Third description here.'
//   }
// ];

class App extends Component {
  state = {
    data: []
    
  };


  render() {
    console.log("rendering!");
    return (
      <div>
        
        <Fragment>

        <Head/>
        <AuthorList/>

    
        <Home/>
        </Fragment>
      </div>
    );
  }
}



// {this.state.data.map(item => (
//  <div key={item.id}>
//  <h1>{item.name}</h1>
// <span>{item.affiliation}</span>
//</div>
//))}
// import React from 'react';
// import logo from './logo.svg';
// import './App.css';
//
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
