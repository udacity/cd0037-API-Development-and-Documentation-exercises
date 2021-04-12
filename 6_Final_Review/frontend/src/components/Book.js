import React, { Component } from 'react';

import '../stylesheets/Book.css';

const starArray = [5,4,3,2,1]

class Book extends Component {
  createStars(){
    let {id, rating, deleteBook} = this.props;

    return ( 
      <div className="rating">
        {starArray.map(num => (
          <div
            key={num}
            onClick={() => {this.props.changeRating(this.props.id, num)}}
            className={`star ${rating >= num ? 'active':''}`}
          />
        ))}
        <div className="delete" onClick={() => {deleteBook(id)}} />
      </div>
    )
  }

  render() {
    let {title, author} = this.props;

    return (
      <div className="book">
        <div className="cover">
            <div className="title">{title}</div>
        </div>
        <div className="author">
            {author}
        </div>
        {this.createStars()}
      </div>
    );
  }
}

export default Book;
