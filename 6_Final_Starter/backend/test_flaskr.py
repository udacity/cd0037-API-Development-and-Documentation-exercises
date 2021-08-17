import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book

# TODO: Create BookTestCase class
# Use the create_app method to create an app, access the test client, and set up the database
# Also define the object you'll use to test the POST endpoint for a new book
# TODO: define setUp and tearDown methods
# TODO: Write at minimum one test case for each endpoint you wrote
# TODO: Write at minimum one test case per errorhandler created


# TODO: Before implementing the endpoint, write new tests for handling search
# TODO: Run the tests to ensure that your old tests still work, or fail predictably and the new test fails


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "student", "student", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        self.new_book = {"title": "Anansi Boys", "author": "Neil Gaiman", "rating": 5}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_paginated_books(self):
        res = self.client().get("/books")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_books"])
        self.assertTrue(len(data["books"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/books?page=1000", json={"rating": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_get_book_search_with_results(self):
        res = self.client().post("/books", json={"search": "Novel"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_books"])
        self.assertEqual(len(data["books"]), 2)

    def test_get_book_search_without_results(self):
        res = self.client().post("/books", json={"search": "applejacks"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_books"], 0)
        self.assertEqual(len(data["books"]), 0)

    def test_update_book_rating(self):
        res = self.client().patch("/books/5", json={"rating": 1})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 5).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(book.format()["rating"], 1)

    def test_400_for_failed_update(self):
        res = self.client().patch("/books/5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    # def test_delete_book(self):
    #     res = self.client().delete('/books/1')
    #     data = json.loads(res.data)

    #     book = Book.query.filter(Book.id == 1).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 1)
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))
    #     self.assertEqual(book, None)

    def test_404_if_book_does_not_exist(self):
        res = self.client().delete("/books/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_create_new_book(self):
        res = self.client().post("/books", json=self.new_book)
        data = json.loads(res.data)
        pass

    def test_422_if_book_creation_fails(self):
        res = self.client().post("/books", json=self.new_book)
        data = json.loads(res.data)
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
