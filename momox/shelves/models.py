from momox.app import db
from momox.books.models import Book


class Shelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = db.relationship('Book', backref='shelf.id', lazy=True)
