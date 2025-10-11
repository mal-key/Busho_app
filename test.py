import json
import pprint
from pathlib import Path
import csv
import re

all_busho_list = []  # 一番外側用の空リストを作成
with open("./busho.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        list_delete_blank = list(filter(None, row))  # 空白を除いたもの
        for l in list_delete_blank:
            p = re.compile("[\u3041-\u309f]+")
            try:
                if p.fullmatch(l):  # 要素がすべてひらがなだった時の処理
                    busho_dict = {}  # 各武将データ格納用の空の辞書を作成
                    name_kana = l
                    name_kana_index = list_delete_blank.index(
                        l
                    )  # lの値がlist_delete_blank内で何番目か検索
                    name = list_delete_blank[
                        name_kana_index - 1
                    ]  # 取得した番号の一つ前の要素を取得
                    birth_year = list_delete_blank[
                        name_kana_index + 1
                    ]  # 取得した番号の一つあとの要素を取得（生年）
                    death_year = list_delete_blank[
                        name_kana_index + 3
                    ]  # 取得した番号の3つあとの要素を取得（没年）
                    busho_id = list_delete_blank[
                        0
                    ]  # list_delete_blankの一番目要素を取得
                    busho_dict.update(
                        busho_id=int(busho_id),
                        name=name,
                        name_kana=name_kana,
                        birth_year=int(birth_year),
                        death_year=int(death_year),
                    )
                    # 各武将データをbusho_dictへ格納
                    all_busho_list.append(
                        busho_dict
                    )  # 一番外側のリストに武将データ格納用リストを格納
            except (IndexError, ValueError):
                pass

        count += 1
        # if count > 10:
        #     break
# pprint.pprint(all_busho_list, sort_dicts=False)

with open("./busho.json", "w", encoding="utf-8") as f:
    json.dump(all_busho_list, f, indent=2, ensure_ascii=False)
# 同じディレクトリにbusho.jsonとして保存


# ・数値をintに変換
# ・全データを出力
