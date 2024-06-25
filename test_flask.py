#!/usr/bin/python3

from routes import app
from models.base_model import db

with app.app_context():
    db.create_all()
