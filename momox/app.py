from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


FILE_PATH = Path.cwd() / "database.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
