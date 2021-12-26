from sqlalchemy.ext.hybrid import hybrid_property

from momox.constants import Status
from app import db


class Shelf(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    books = db.relationship('Book', backref='shelf.id', lazy=True)

    def as_dict(self):
        return {
            "id": self.id,
            "books": [book.as_dict() for book in self.books]  # or just IDs
        }


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(120), nullable=False)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id'), nullable=True)

    @hybrid_property
    def status(self):
        if self.price:
            return Status.PRESENT if self.shelf_id else Status.SOLD
        return Status.HOLD

    def as_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
            "shelf_id": self.shelf_id,
            "status": self.status
        }
