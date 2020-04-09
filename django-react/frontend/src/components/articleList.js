import React, { Component } from "react";
import { Table } from "reactstrap";
import NewArticleModal from "./newArticleModal";
import ConfirmRemovalModal from "./ConfirmModalRemoval";


class ArticleList extends Component {
  render() {
    const articles = this.props.articles;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Article_Name</th>
            <th>Affiliation</th>
            <th>pub_title</th>
            <th>pub_year</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!articles || articles.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, none here yet</b>
              </td>
            </tr>
          ) : (
            articles.map(article => (
              <tr key={article.name}>
                <td>{article.name}</td>
                <td>{article.affiliation}</td>
                <td>{article.pub_title}</td>
                <td>{article.pub_year}</td>
                <td align="center">
                  <NewArticleModal
                    create={false}
                    article={article}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    name={article.name}
                    affiliation={article.affiliation}
                    pub_title = {article.pub_title}
                    pub_year = {article.pub_year}
                    resetState={this.props.resetState}
                  />
                  
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default ArticleList;