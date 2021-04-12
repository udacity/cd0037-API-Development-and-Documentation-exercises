import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy #, or_
from flask_cors import CORS

from models import setup_db, Book

BOOKS_PER_SHELF = 8

# TODO: Define the create_app method and complete initial set up of the application
# TODO: Enable CORS and set response headers
# TODO: Define an app route to retrieve all books
# TODO: Define pagination behavior on the get request

# TODO: Define an endpoint to delete a book based on id. If it doesn't exist, abort. 
# TODO: Define a PATCH endpoint that updates a book's rating. 
  # Abort if the book doesn't exist or the update fails 
# TODO: Define a POST endpoint to handle creating a new book instance.
  # Abort if creation is unsuccessful

# TODO: Write error handlers for all abort status codes utilized in the endpoints
  # They should return the code, a message, and success value. 

# TODO: AFTER writing the corresponding tests, write an endpoint or update a previous endpoint
  # that handles a search arg in the body of the request and return paginated results. 




def paginate_books(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * BOOKS_PER_SHELF
  end = start + BOOKS_PER_SHELF

  books = [book.format() for book in selection]
  current_books = books[start:end]

  return current_books

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  
  @app.route('/books')
  def retrieve_books():
    selection = Book.query.order_by(Book.id).all()
    current_books = paginate_books(request, selection)

    if len(current_books) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'books': current_books,
      'total_books': len(Book.query.all())
    })
    
  # @app.route('/books/<int:book_id>')
  # def retrieve_book(book_id):
  #   book = Book.query.filter(Book.id == book_id).one_or_none()
  #   if book is None:
  #     abort(404)
  #   else:
  #     return jsonify({
  #       'success': True,
  #       'book': book.format()
  #     })

  @app.route('/books/<int:book_id>', methods=['PATCH'])
  def update_book(book_id):

    body = request.get_json()

    try:
      book = Book.query.filter(Book.id == book_id).one_or_none()
      if book is None:
        abort(404)

      if 'rating' in body:
        book.rating = int(body.get('rating'))

      book.update()

      return jsonify({
        'success': True,
      })
      
    except:
      abort(400)

  @app.route('/books/<int:book_id>', methods=['DELETE'])
  def delete_book(book_id):
    try:
      book = Book.query.filter(Book.id == book_id).one_or_none()

      if book is None:
        abort(404)

      book.delete()
      selection = Book.query.order_by(Book.id).all()
      current_books = paginate_books(request, selection)

      return jsonify({
        'success': True,
        'deleted': book_id,
        'books': current_books,
        'total_books': len(Book.query.all())
      })

    except:
      abort(422)

  @app.route('/books', methods=['POST'])
  def create_book():
    body = request.get_json()

    new_title = body.get('title', None)
    new_author = body.get('author', None)
    new_rating = body.get('rating', None)
    search = body.get('search', None)

    try:
      if search:
        selection = Book.query.order_by(Book.id).filter(Book.title.ilike('%{}%'.format(search)))
        #selection = Book.query.order_by(Book.id).filter(or_(Book.title.ilike('%{}%'.format(search)), Book.author.ilike('%{}%'.format(search))))
        current_books = paginate_books(request, selection)

        return jsonify({
          'success': True,
          'books': current_books,
          'total_books': len(selection.all())
        })
      else: 
        book = Book(title=new_title, author=new_author, rating=new_rating)
        book.insert()

        selection = Book.query.order_by(Book.id).all()
        current_books = paginate_books(request, selection)

        return jsonify({
          'success': True,
          'created': book.id,
          'books': current_books,
          'total_books': len(Book.query.all())
        })

    except:
      abort(422)

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400
  
  return app

    