from flask import Blueprint, render_template, session, request
from app.models import db, Busho
import random

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
    # sessionに読み仮名を保存（正解判定用）
    session["correct_answer_kana"] = random_busho.name_kana
    # ページとランダムに取得した武将名を返す
    return render_template("quiz/quiz-input.html", random_busho_name=random_busho.name)


# 解答送信
@quiz_bp.route("/input", methods=["POST"])
def quiz_input():
    answer = request.form["answer"]  # quiz-input.htmlで入力された値を取得
    correct_answer_kana = session.get(
        "correct_answer_kana"
    )  # sessionに保存していた読み仮名データを取得
    if (
        answer == correct_answer_kana
    ):  # 入力された値が正解の読み仮名と合致しているか判定
        result = "correct"
    else:
        result = "wrong"
    return render_template(
        "quiz/quiz-input.html",
        correct_answer_kana=correct_answer_kana,
        result=result,
    )


# 武将没年クイズページ
@quiz_bp.route("/choice", methods=["GET"])
def quiz_choice_page():
    # dbからランダムに武将名を取得
    random_bushos = Busho.query.order_by(db.func.random()).limit(4).all()
    # ランダムに取得した中から正解を設定する
    correct_busho = random.choice(random_bushos)
    # 正解の名前と没年をsessionに保存
    session["correct_busho_deathyear"] = correct_busho.death_year
    session["correct_busho_name"] = correct_busho.name

    # 選択肢リストに取得した没年を入れ、選択肢を4つ作成
    choice_list = []
    for busho in random_bushos:
        choice_list.append(busho.death_year)
    random.shuffle(choice_list)  # 選択肢をシャッフル

    # ページとランダムに取得した武将名を返す
    return render_template(
        "quiz/quiz-choice.html",
        correct_busho_name=correct_busho.name,
        choice_list=choice_list,
    )


# 武将没年解答
@quiz_bp.route("/choice", methods=["POST"])
def quiz_choice():
    answer = request.form["answer"]  # quiz-choice.htmlで入力された値を取得
    correct_busho_deathyear = session.get(
        "correct_busho_deathyear"
    )  # sessionに保存していた没年データを取得
    if answer == str(
        correct_busho_deathyear
    ):  # 入力された値を文字列に変換し、正解と合致しているか判定
        result = "correct"
    else:
        result = "wrong"
    return render_template(
        "quiz/quiz-choice.html",
        correct_busho_deathyear=correct_busho_deathyear,
        result=result,
    )
