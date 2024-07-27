from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '4d297f88daf6623e4fe0df5f62d1e152c2076978af7ae82c4f77006340f256f1'
app.config['UPLOAD_FOLDER'] = 'static/user_images'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

USER = os.getenv('USER', 'Name')
PWD = os.getenv('PWD', 'Password')
HOST = os.getenv('HOST', 'localhost')
DB = os.getenv('DB', 'Healixra')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER}:{PWD}@{HOST}/{DB}'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'