from flask import Flask, Blueprint
from app.models import db
from pathlib import Path

from app.bushocrud import bp

app = Flask(__name__)
app.register_blueprint(bp)

# bushoapp.py ファイルのある場所（appディレクトリ）を基準に絶対パスを作る
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "instance" / "busho.db"  # DBファイルの場所を指定


# SQLiteデータベースの設定
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Flaskアプリとmodels.pyのDBを紐づける
db.init_app(app)


# Hello World用のルート
@app.route("/")
def hello():
    return "Hello, World!"
