import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ArticleList from "./articleList";
import NewArticleModal from "./newArticleModal";

import axios from "axios";



class Home extends Component {
  state = {
    articles: []
  };

  componentDidMount() {
    this.resetState();
  }

  getArticles = () => {
    axios.get("http://127.0.0.1:8000/api/articles/all").then(res => this.setState({ articles: res.data }));
  };

  resetState = () => {
    this.getArticles();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px", marginBottom: "100px"}}>
        <Row>
          <Col>
            <ArticleList
              articles={this.state.articles}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewArticleModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;