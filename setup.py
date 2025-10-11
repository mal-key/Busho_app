# 初期設定スクリプト（テープル初期化とjsonファイルのインポート）
import json
from app import bushoapp
from app.models import db, Busho
from pathlib import Path

# DBファイルのパスとinstanceディレクトリの確認
INSTANCE_DIR = Path(__file__).resolve().parent / "app" / "instance"
INSTANCE_DIR.mkdir(parents=True, exist_ok=True)  # instanceディレクトリがなければ作成


def init_db():
    """SQLiteのDBとテーブルを初期化"""
    with bushoapp.app.app_context():
        db.create_all()  # models.pyの定義に基づいてテーブル作成


def import_json():
    """busho.jsonのデータをDBにインポート"""
    json_path = Path(__file__).resolve().parent / "busho.json"
    # Flaskに「このアプリを使う」ことを伝える（アプリケーションコンテキストの有効化）
    with bushoapp.app.app_context():
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            for item in data:  # ループで1件ずつBushoモデルに変換
                busho = Busho(
                    busho_id=item["busho_id"],
                    name=item["name"],
                    name_kana=item["name_kana"],
                    birth_year=item["birth_year"],
                    death_year=item["death_year"],
                )
                db.session.add(busho)  # Bushoモデルのインスタンスをセッションに追加
            db.session.commit()  # セッションに追加された全ての変更をまとめてDBに反映


if __name__ == "__main__":
    init_db()  # DBとテーブルの初期化
    import_json()  # jsonファイルのデータをインポート
