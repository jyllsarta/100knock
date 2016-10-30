# -*- coding: utf-8 -*-
"""25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートの
フィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import re

if __name__ == "__main__":
    filepath = "03/data/britain.txt"
    with open(filepath,"r",encoding="utf-8")as file:
        text = file.read()

    template = {}

    regexp = "^\|(.*) = (.*(.|\n^(\*))*)"

    result = re.finditer(regexp,text,re.MULTILINE)

    for item in result:
        template[item.group(1)] = item.group(2) 

    print(template)