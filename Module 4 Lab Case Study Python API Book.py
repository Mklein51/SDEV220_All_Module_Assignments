from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"
    
@app.route('/')
def index():
    return 'Book API Created'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = { 'id': book.id, 'book_name': book.book_name, 'author': book.author,'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route('/books')
def add_book():
    book_data = request.get_json()
    new_book = Book( book_name=book_data['book_name'], author=book_data['author'], publisher=book_data['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return {"id": new_book.id}

@app.route('/books/<int:id>')
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book not found"}
    db.session.delete(book)
    db.session.commit()


