from flask import Blueprint, render_template, request
from app.models import db, Busho

# Blueprintオブジェクトを作成
# 第1引数："quiz"はBlueprintの名前（アプリ内で一意であれば自由）
# 第2引数：__name__ は現在のモジュール名（Blueprintの内部参照に使用）
# url_prefix="/quiz" はこのBlueprintは以下のURLはすべて/quizから始まる
quiz_bp = Blueprint("quiz", __name__, url_prefix="/quiz")


# 武将読み仮名クイズページ
@quiz_bp.route("/input", methods=["GET"])
def quiz_input_page():
    # dbからランダムに武将名を取得
    random_busho = Busho.query.order_by(db.func.random()).first()
    # ページとランダムに取得した武将名を返す
    return render_template("quiz/quiz-input.html", random_busho_name=random_busho.name)


# 解答送信
@quiz_bp.route("/input", methods=["POST"])
def quiz_input():
    # quiz-inputで入力された値を取得し、
    # 入力された値がbusho-kanaと合致しているかチェック
    # 合致していたら正解判定
    # 合致していなかったら不正解判定
    messaege = "解答しました"
    return messaege


# 武将没年クイズページ
@quiz_bp.route("/choice", methods=["GET"])
def quiz_choice_page():
    # dbからランダムに武将名を取得
    random_busho = Busho.query.order_by(db.func.random()).first()
    # ページとランダムに取得した武将名を返す
    return render_template("quiz/quiz-choice.html", random_busho_name=random_busho.name)


# 武将没年解答
@quiz_bp.route("/choice", methods=["POPST"])
def quiz_choice():
    # 選択された解答がdeath_yearと合致しているかチェック
    # 合致していたら正解判定
    # 合致していなかったら不正解判定
    messaege = "解答しました"
    return messaege
