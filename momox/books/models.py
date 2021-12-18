from sqlalchemy.ext.hybrid import hybrid_property

from momox.app import db
from momox.books.constants import Status


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
