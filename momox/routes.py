import json

from flask import request
from flask import current_app as app

from app import db
from momox.models import Shelf, Book


@app.route('/shelves', methods=['POST'])
def shelves_post():
    shelf = Shelf(books=request.json.get('books', []))
    db.session.add(shelf)
    db.session.commit()

    return app.response_class(
        response=json.dumps(shelf.as_dict()),
        status=201,
        mimetype='application/json'
    )


@app.route('/books', methods=['POST'])
def books_post():
    book = Book(
        price=request.json.get('price', None),
        name=request.json.get('name'),
        shelf_id=request.json.get('shelf_id', None),
    )
    db.session.add(book)
    db.session.commit()

    return app.response_class(
        response=json.dumps(book.as_dict()),
        status=201,
        mimetype='application/json'
    )
