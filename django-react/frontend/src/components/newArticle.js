import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

const API_URL_CREATE = 'http://127.0.0.1:8000/api/articles/add'
const API_URL_EDIT = 'http://127.0.0.1:8000/api/articles/update'
//const API_URL_DELETE = 'http://127.0.0.1:8000/api/articles/delete/'

class NewArticle extends React.Component {
  state = {
    name : "",
    affiliation : "",
    pub_title : "",
    pub_year : ""
  };

  componentDidMount() {
    if (this.props.article) {
      const {name,affiliation,pub_title,pub_year} = this.props.article;
      this.setState({name,affiliation,pub_title,pub_year});
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createArticle = e => {
    e.preventDefault();

    const data = {
      name: this.state.name,
      affiliation: this.state.affiliation,
      pub_title: this.state.pub_title,
      pub_year: this.state.pub_year

    }
    axios.post(API_URL_CREATE, data).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editArticle = e => {
    e.preventDefault();
    axios.put(API_URL_EDIT,
      {name: this.state.name, affiliation:this.state.affiliation,pub_title:this.state.pub_title,pub_year:this.state.pub_year}).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.article ? this.editArticle : this.createArticle}>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="affiliation">affiliation:</Label>
          <Input
            type="text"
            name="affiliation"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.affiliation)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="pub_title">pub_title:</Label>
          <Input
            type="text"
            name="pub_title"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.pub_title)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="pub_year">pub_year:</Label>
          <Input
            type="text"
            name="pub_year"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.pub_year)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewArticle;