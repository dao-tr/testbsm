import os
import cloudinary
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.secret_key = 'BOOKSTORE_SECRET_KEY_2026!@#'

db_url = os.environ.get('DATABASE_URL')
if db_url and db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url or 'mysql+pymysql://root:%s@localhost/bookstoredb?charset=utf8mb4' % quote('Tmd.1603')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PAGE_SIZE'] = 8

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(
    cloud_name='dsjytfvdz',
    api_key='841864179767685',
    api_secret='HSKtnNsA6UtWZvlI-w24ef99UD4'
)

# Luôn đặt các import này ở dòng cuối cùng của file
from app import admin, utils, index