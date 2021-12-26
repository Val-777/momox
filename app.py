from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# Path to the db file
FILE_PATH = Path.cwd() / "database.db"


def create_app():
    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{FILE_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from momox import routes  # Register routes
        db.create_all()

        return app
