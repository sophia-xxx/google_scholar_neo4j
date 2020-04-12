import React, { Component } from "react";
import { Table, Button } from "reactstrap";

import '../App.css'


import axios from "axios";

class AuthorList extends Component {
    state = {
        data:[]
    };

    async mounting(InputName) {
        InputName = InputName.split(' ').join('+');
        if (InputName.length > 0) {
            try {
                const res = await fetch('http://127.0.0.1:8000/api/authors/name='+InputName);
                const data = await res.json();
                console.log("api success!");
                this.setState({
                  data
                });
              } catch (e) {
                console.log(e);
              }
        } else {
            try {
                const res = await fetch('http://127.0.0.1:8000/api/authors/all');
                const data = await res.json();
                console.log("api success!");
                this.setState({
                  data
                });
              } catch (e) {
                console.log(e);
              }
        }
        
      }

      render() {
        return (
            <div style={{ marginTop: "50px",marginLeft: "40vh",marginRight:"40vh" }}>
                
            <input type="text" class="myform" id="InputName" placeholder="Enter name"></input>
            <Button style={{ marginLeft: "10px"}}color="primary" onClick={() => this.mounting(document.getElementById('InputName').value)}>
          Search
        </Button>
          <Table dark>
            <thead>
              <tr>
                <th>Author_Name</th>
                <th>Author_Affiliaiton</th>
              </tr>
            </thead>
            <tbody>
              {!this.state.data || this.state.data.length <= 0 ? (
                <tr>
                  <td colSpan="6" align="center">
                    <b>No Author Exists :(</b>
                  </td>
                </tr>
              ) : (
                this.state.data.map(article => (
                  <tr key={article.name}>
                    <td>{article.name}</td>
                    <td>{article.affiliation}</td>
                    
                  </tr>
                ))
              )}
            </tbody>
          </Table>
            </div>
        );
    }

}

export default AuthorList;