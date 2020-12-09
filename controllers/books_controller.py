from flask import Flask, render_template, request, redirect, Blueprint
from repositories import author_repository
from repositories import book_repository
from models.author import Author
from models.book import Book

books_blueprint = Blueprint('books', __name__)


# NEW
# GET '/books/new'

# CREATE
# POST '/books'
@books_blueprint.route('/books', methods = ['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author = author_repository.select(author_id)
    book = Book(title, genre, publisher)
    book_repository.save(book)
    return redirect('/books')




# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'

