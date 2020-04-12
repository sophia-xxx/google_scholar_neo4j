import React, { Component, Fragment } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

const API_URL = 'http://127.0.0.1:8000/api/articles/delete'

class ConfirmRemovalModal extends Component {
  state = {
    modal: false

  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
    
  };

    deleteArticle = (name,affiliation,pub_title) => {
        const name_WithoutSpace = name.split(' ').join('+');
        const affiliation_WithoutSpace = affiliation.split(' ').join('+');
        const pub_title_WithoutSpace = pub_title.split(' ').join('+');

        

        axios.delete(API_URL, {
            data: { name: name_WithoutSpace, affiliation:affiliation_WithoutSpace, pub_title:pub_title_WithoutSpace  }
           }).then(() => {
        this.props.resetState();
        this.toggle();
        window.location.reload();
        });
  };

  render() {
    return (
      <Fragment>
        <Button color="danger" onClick={() => this.toggle()}>
          Remove
        </Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>
            Do you really want to delete the article?
          </ModalHeader>

          <ModalFooter>
            <Button type="button" onClick={() => this.toggle()}>
              Cancel
            </Button>
            <Button
              type="button"
              color="primary"
              onClick={() => this.deleteArticle(this.props.name, this.props.affiliation,this.props.pub_title)}
            >
              Yes
            </Button>
          </ModalFooter>
        </Modal>
      </Fragment>
    );
  }
}

export default ConfirmRemovalModal;