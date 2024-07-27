#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# from flask_sqlalchemy import SQLAlchemy
# from routes import app
import os

# db = SQLAlchemy(app)

if os.getenv('TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()