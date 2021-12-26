import json

from flask import request, abort
from flask import current_app as app

from app import db
from momox.models import Shelf, Book


@app.route('/shelves', methods=['POST'])
def shelves_post():
    # Request validation happening here
    shelf = Shelf()
    db.session.add(shelf)
    db.session.commit()

    return app.response_class(
        response=json.dumps(shelf.as_dict()),
        status=201,
        mimetype='application/json'
    )


@app.route('/books', methods=['POST'])
def books_post():
    # Request validation happening here
    book = Book(
        price=request.json.get('price'),
        name=request.json.get('name'),
        shelf_id=request.json.get('shelf_id', None)
    )
    db.session.add(book)
    db.session.commit()

    return app.response_class(
        response=json.dumps(book.as_dict()),
        status=201,
        mimetype='application/json'
    )


@app.route('/shelf/<int:_id>', methods=['GET'])
def shelf_get(_id):
    shelf = Shelf.query.get(_id)

    if shelf:
        return app.response_class(
            response=json.dumps(shelf.as_dict()),
            mimetype='application/json'
        )
    else:
        abort(404)


@app.route('/book/<int:_id>', methods=['GET'])
def book_get(_id):
    book = Book.query.get(_id)

    if book:
        return app.response_class(
            response=json.dumps(book.as_dict()),
            mimetype='application/json'
        )
    else:
        abort(404)


@app.route('/book/<int:_id>', methods=['PATCH'])
def book_patch(_id):
    book = Book.query.get(_id)

    if book:
        if 'price' in request.json.keys():
            book.price = request.json.get('price')
        if 'name' in request.json.keys():
            book.name = request.json.get('name')
        if 'shelf_id' in request.json.keys():
            book.shelf_id = request.json.get('shelf_id')

        db.session.add(book)
        db.session.commit()

        return app.response_class(
            response=json.dumps(book.as_dict()),
            mimetype='application/json'
        )
    else:
        abort(404)


@app.route('/book/<int:_id>', methods=['DELETE'])
def book_delete(_id):
    book = Book.query.get(_id)

    if book:

        Book.query.filter_by(id=_id).delete()
        db.session.commit()

        return app.response_class(
            response='',
            status=204,
            mimetype='application/json'
        )
    else:
        abort(404)
