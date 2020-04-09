import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="https://logopond.com/logos/eb98c5a0f4ce70bdd1191c858485b80d.png"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h1>Google Scholarly Database</h1>
        <h5>
          <i>by Arman, Lucasz, Nidhi, Sophia</i>
        </h5>
        
      </div>
    );
  }
}

export default Header;