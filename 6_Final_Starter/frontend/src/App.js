import React, { Component } from 'react';
import $ from 'jquery';

import './stylesheets/App.css';
import FormView from './components/FormView';
import Book from './components/Book';


class App extends Component {
  constructor(props){
    super();
    this.state = {
      page: 1,
      totalBooks: 0,
      books: []
    }
  }

  getBooks = () => {
    $.ajax({
      url: `/books?page=${this.state.page}`, //TODO: update request URL
      type: "GET",
      success: (result) => {
        this.setState({
          totalBooks: result.total_books,
          books: result.books 
        })
        return;
      },
      error: (error) => {
        alert('Unable to load books. Please try your request again')
        return;
      }
    })
  }

  deleteBook = (id) => {
    if(window.confirm('Are you sure you want to delete the book?')) {
      $.ajax({
        url: `/books/${id}`, //TODO: update request URL
        type: "DELETE",
        success: (result) => {
          this.getBooks();
        },
        error: (error) => {
          alert('Unable to delete the book.')
          return;
        }
      })
    }
  }

  changeRating = (id, rating) => {
    let books = [...this.state.books]
    let targetBook = books.find((book) => book.id === id);

    $.ajax({
      url: `/books/${id}`, //TODO: update request URL
      type: "PATCH",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({'rating': rating}),
      success: (result) => {
        targetBook.rating = rating
        this.setState({books})
      },
      error: (error) => {
        alert('Unable to update the rating.')
        return;
      }
    })
  }

  searchBooks = (search) => {
    $.ajax({
      url: '/books', //TODO: update request URL
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({search: search}),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          totalBooks: result.total_books,
          books: result.books,
          page: 1
        })
        document.getElementById("search-form").reset();
        return;
      },
      error: (error) => {
        alert('Unable to complete search. Please try your request again')
        return;
      }
    })
  }

  
  componentDidMount(){
    this.getBooks()
  }

  selectPage(num) {
    this.setState({page: num}, () => this.getBooks());
  }

  createPagination(){
    let pageNumbers = [];
    let maxPage = Math.ceil(this.state.totalBooks / 8)
    for (let i = 1; i <= maxPage; i++) {
      pageNumbers.push(
        <div
          key={i}
          className={`page-num ${i === this.state.page ? 'active' : ''}`}
          onClick={() => {this.selectPage(i)}}>{i}
        </div>)
    }
    return pageNumbers;
  }

  render() {
    return (
      <div className="App">
        <div id="main-view">
          <div className="bookshelf-container">
            {this.state.books.map((book) => (
              <Book
                key={book.id}
                deleteBook={this.deleteBook}
                changeRating={this.changeRating}
                {...book}
              />
            ))}
          </div>
          <div className="pagination-menu">
              {this.createPagination()}
          </div>
        </div>
        <FormView searchBooks={this.searchBooks}/>
      </div>
    );

  }
}

export default App;
