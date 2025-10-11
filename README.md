## 開発環境のセットアップ

**依存パッケージのインストール**
```bash
pip install -r requirements.txt
```
**データベースの初期化 & JSON データのインポート**
```bash
python3 setup.py
```
**SQLite の中身を確認**
```bash
sqlite3 app/instance/busho.db
.table
SELECT \* FROM busho LIMIT 5;
```
## 開発サーバーの起動
```bash
flask --app app.bushoapp run
```
## ディレクトリ構成
```plaintext
project_root/
├── app/
│ ├── **init**.py
│ ├── bushoapp.py ← Flask アプリ本体
│ ├── models.py ← DB テーブル定義（SQLAlchemy）
│ └── instance/
│ └── busho.db ← 自動生成される SQLite DB（setup.py で作成）
├── busho.json ← JSON 形式の初期データ
├── setup.py ← DB 作成 & JSON インポートの初期設定スクリプト
├── requirements.txt
└── README.md
