## 使用技術 ##
| カテゴリ    | 内容                        |
| ------- | ------------------------- |
| 言語      | Python 3.13               |
| フレームワーク | Flask 3.1.2                   |
| データベース  | SQLite3（SQLAlchemy）       |
| 開発環境    | venv（仮想環境）                |
| その他     | Git / Jinja2 / HTMLテンプレート |

## 目的 ##
- バックエンド開発の練習
- Flaskの構成理解（ルーティング・テンプレート・DB連携）
- コード設計・関数化・ファイル分割の練習

## 機能概要 ##
| 機能	| 内容 |
| ------- | ------------------------- |
|CRUD機能	| 武将データの登録・編集・削除 |
|クイズ機能	| 武将名をランダム出題し、入力解答を判定 |
|データ入出力	| CSVから登録、JSON形式で出力 |

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
SELECT * FROM busho LIMIT 5;
```
## 開発サーバーの起動
**通常モード：**
```bash
flask --app app.bushoapp run
```
**デバッグモード：**
```bash
flask --app app.bushoapp --debug run
```
## ディレクトリ構成
```plaintext
project_root/
├── app/
│   ├── __init__.py
│   ├── bushoapp.py  # Flaskアプリ本体（エントリーポイント）
│   ├── bushocrud.py # CRUD機能（登録・一覧・詳細・編集・削除）
│   ├── bushoquiz.py # クイズ機能（ランダム出題・入力式/選択式回答および回答判定）
│   ├── instance
│   │   └── busho.db # 自動生成される SQLite DB（setup.py で作成）
│   ├── models.py    # DB テーブル定義（SQLAlchemy）
│   └── templates
│       ├── base.html
│       ├── crud
│       │   ├── create.html
│       │   ├── detail.html
│       │   ├── list.html
│       │   └── update.html
│       ├── home.html
│       └── quiz
│           ├── quiz-choice.html
│           └── quiz-input.html
├── busho.json   # JSON形式の初期データ
├── setup.py     # DB作成 & JSONインポートの初期設定スクリプト
├── requirements.txt
└── README.md
