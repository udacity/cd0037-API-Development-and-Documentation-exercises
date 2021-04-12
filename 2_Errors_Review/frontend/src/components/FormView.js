import React, { Component } from 'react';
import $ from 'jquery';

import '../stylesheets/FormView.css';

class FormView extends Component {
  constructor(props){
    super();
    this.state = {
      title: "",
      author: "",
      rating: 1,
      search: '',
    }
  }

  submitBook = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/books', //TODO: update request URL
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        title: this.state.title,
        author: this.state.author,
        rating: this.state.rating,
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        document.getElementById("add-book-form").reset();
        return;
      },
      error: (error) => {
        alert('Unable to add book. Please try your request again')
        return;
      }
    })
  }

  handleSearch = (event) => {
    event.preventDefault();
    this.props.searchBooks(this.state.search);
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }

  render() {
    return (
      <div id="form-view">
        <div className="search" style={{'display': 'None'}}>
          <h2>Search</h2>
          <form className="FormView" id="search-form" onSubmit={this.handleSearch}>
            <input type="text" name="search" onChange={this.handleChange}/>
            <input type="submit" className="button" value="Submit" />
          </form>
        </div>
        <h2>Add a New Book</h2>
        <form className="FormView" id="add-book-form" onSubmit={this.submitBook}>
          <label>
            Title
            <input type="text" name="title" onChange={this.handleChange}/>
          </label>
          <label>
            Author
            <input type="text" name="author" onChange={this.handleChange}/>
          </label>
          <label>
            Rating
            <select name="rating" onChange={this.handleChange}>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
          </label>
          <input type="submit" className="button" value="Submit" />
        </form>
      </div>
    );
  }
}

export default FormView;
