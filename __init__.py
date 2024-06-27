from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '4d297f88daf6623e4fe0df5f62d1e152c2076978af7ae82c4f77006340f256f1'

# Use environment variables to configure your MySQL connection
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER', 'Name')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD', 'Password')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST', 'localhost')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB', 'Healixra')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
