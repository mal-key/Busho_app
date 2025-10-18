from flask import Blueprint, render_template, request
from sqlalchemy import desc

from app.models import db, Busho


crud_bp = Blueprint("crud", __name__, url_prefix="/crud")


# 武将作成ページ
@crud_bp.route("/create", methods=["GET"])
def create_page():
    return render_template("crud/create.html")


# 武将作成
@crud_bp.route("/create", methods=["POST"])
def create():
    form_data = request.form.to_dict()
    # 割り当てるbusho_idを取得する
    busho_data = Busho.query.order_by(desc(Busho.busho_id)).first()
    max_busho_id = busho_data.busho_id

    busho = Busho(
        busho_id=max_busho_id + 1,
        name=form_data["name"],
        name_kana=form_data["name_kana"],
        birth_year=form_data["birth_year"],
        death_year=form_data["death_year"],
    )
    db.session.add(busho)  # Bushoモデルのインスタンスをセッションに追加
    db.session.commit()  # セッションに追加された全ての変更をまとめてDBに反映

    message = f"{form_data['name']}が登録されました"

    return render_template("crud/create.html", message=message)


# 武将一覧ページ
@crud_bp.route("/list", methods=["GET"])
def bussho_list():
    busho_data = Busho.query.all()
    busho_list = []
    for busho in busho_data:
        data = {"busho_id": busho.busho_id, "name": busho.name}
        busho_list.append(data)

    return render_template("crud/list.html", busho_list=busho_list)


# 武将詳細ページ
@crud_bp.route("/detail/<busho_id>", methods=["GET"])
def busho_detail(busho_id):
    # パスパラメータからbusho_idを取得
    print(busho_id)

    # busho_idから武将データを取得
    # フロントに渡す
    return


# 武将更新
@crud_bp.route("/update", methods=["POST"])
def update():
    return


# 武将削除
@crud_bp.route("/delete", methods=["POST"])
def delete():
    return
