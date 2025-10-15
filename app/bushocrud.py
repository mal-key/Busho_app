from flask import Blueprint, render_template, request
from app.models import Busho


bp = Blueprint("crud", __name__, url_prefix="/crud")


@bp.route("/", methods=["GET"])
def crud_home():
    return render_template("crud/home.html")


# 武将作成ページ
@bp.route("/create", methods=["GET"])
def create_page():
    return render_template("crud/create.html")


# 武将作成
@bp.route("/create", methods=["POST"])
def create():
    print(request.form.to_dict())
    form_data = request.form.to_dict()
    # {'name': 'ヨウ', 'name_kana': 'you', 'birth_year': '1999', 'death_year': '2050'}
    # 割り当てるbusho_idを取得する処理
    busho = Busho(
                    busho_id=form_data["busho_id"],
                    name=form_data["name"],
                    name_kana=form_data["name_kana"],
                    birth_year=form_data["birth_year"],
                    death_year=form_data["death_year"],
                )
                db.session.add(busho)  # Bushoモデルのインスタンスをセッションに追加
            db.session.commit()  # セッションに追加された全ての変更をまとめてDBに反映

    return render_template("crud/create.html")


# 武将一覧表示
@bp.route("/read/<busho_id>", methods=["GET"])
def read():
    return


# 武将更新
@bp.route("/update", methods=["POST"])
def update():
    return


# 武将削除
@bp.route("/delete", methods=["POST"])
def delete():
    return
