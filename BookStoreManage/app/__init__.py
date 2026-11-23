import os
import cloudinary
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.secret_key = 'BOOKSTORE_SECRET_KEY_2026!@#'

# --- Cấu hình Database ---
db_url = os.environ.get('DATABASE_URL')
if db_url and db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url or 'mysql+pymysql://root:%s@localhost/bookstoredb?charset=utf8mb4' % quote('Tmd.1603')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

# Tự động tạo bảng database khi khởi động trên Render
with app.app_context():
    import app.models
    db.create_all()

# --- ĐẶT CÁC IMPORT NÀY Ở DÒNG CUỐI CÙNG CỦA FILE ---
from app import admin, utils, index