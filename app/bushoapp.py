from flask import Flask, Blueprint, render_template, request
from app.models import db
from pathlib import Path

# CRUD機能用とquiz機能用のBlueprintをそれぞれインポート
from app.bushocrud import crud_bp
from app.bushoquiz import quiz_bp

app = Flask(__name__)  # Flaskアプリケーションのインスタンスを作成

# CRUD用とquiz用のBlueprintをアプリに登録（url_prefix=/crud(もしくは/quiz) のルート群を有効化）
app.register_blueprint(crud_bp)
app.register_blueprint(quiz_bp)


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
def home():
    return render_template("home.html")
