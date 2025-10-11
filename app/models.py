from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Busho(db.Model):

    __tablename__ = "busho"

    id = db.Column(db.Integer, primary_key=True)
    busho_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    name_kana = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    death_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):  # デバッグ用の文字列表現を返す
        return f"<Busho {self.name} ({self.busho_id})>"
