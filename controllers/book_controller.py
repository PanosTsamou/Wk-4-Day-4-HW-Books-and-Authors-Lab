
from flask import render_template, redirect, request

from flask import Blueprint
from models.book import Book

import repositories.author_repository as auth_repo
import repositories.book_repository as book_repo

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books ():
    books = book_repo.select_all()
    return render_template("books.jinja", books_to_display = books)

# @books_blueprint.route('/books/delete/<id>', methods=['POST'])
# def delete_book(id):
#     book_repo.delete_by_id(int(id))
#     return redirect('/books')

@books_blueprint.route('/new-book')
def new_book_form():
    authors = auth_repo.select_all()
    return render_template('new_book.jinja', authors = authors)

@books_blueprint.route('/books', methods=['POST'])
def create_new_book():
    book_title = request.form['title']
    book_genre = request.form['genre']
    book_author = request.form['author']
    author = auth_repo.select_by_id(book_author)
    new_book = Book(book_title, book_genre, author)
    book_repo.save(new_book)
    return redirect('/books')

@books_blueprint.route('/books/<id>')
def single_book(id):
    book = book_repo.select_by_id(int(id))
    return render_template('one_book.jinja', book = book)

@books_blueprint.route('/books/<id>/edit')
def edit_book(id):
    book = book_repo.select_by_id(id)
    authors = auth_repo.select_all()
    return render_template('edit.jinja', book = book , authors = authors)

@books_blueprint.route('/books/<id>', methods=['POST'])
def change_book(id):
    book_title = request.form['title']
    book_genre = request.form['genre']
    book_author = request.form['author']
    author = auth_repo.select_by_id(book_author)
    new_book = Book(book_title, book_genre, author, id)
    book_repo.update(new_book)
    return redirect('/books')

@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    print(id)
    book_repo.delete_by_id(int(id))
    return redirect('/books')
