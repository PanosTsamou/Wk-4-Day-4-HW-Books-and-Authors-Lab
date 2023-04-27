from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.author_repository as auth_repo

def save (book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id] 
    book.id= run_sql(sql, values) [0] ['id']
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = auth_repo.select_by_id(row['author_id'])
        # author=auth_repo.select_by_id(row['author_id'])
        book= Book(row['title'], row['genre'], author, row['id'])
        books.append(book)
    return books
def select_author(id):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        author = auth_repo.select_by_id(row['author_id'])
        # author=auth_repo.select_by_id(row['author_id'])
        book= Book(row['title'], row['genre'], author, row['id'])
        books.append(book)
    return books

def select_by_id(id):
    book= None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        author=auth_repo.select_by_id (result['author_id'])
        book= Book(result['title'], result['genre'], author, result['id'])
    return book
    

def update(book):
    sql = "UPDATE books SET (title, genre, author_id) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.author.id, book.id] 
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def delete_by_id(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)