# -*- coding: utf-8 -*-
"""20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．

"""

import json

if __name__ == "__main__":
    filepath = "data/jawiki-country.json"
    with open(filepath,encoding="utf-8") as file:
        #なんか与えられたjsonが構造変だったので各行の末尾に","を付加して読める配列にしてます
        content = file.read()
        wiki = json.loads(content)

    #なんかうまいことやって辞書に直してればすんなりいったのだけど
    for article in wiki:
        if article["title"] == "イギリス":
            article_britain = article["text"]

    with open("03/data/britain.txt","w",encoding="utf-8")as writefile:
        writefile.write(article_britain)