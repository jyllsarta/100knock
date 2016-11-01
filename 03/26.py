# -*- coding: utf-8 -*-
"""26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去して
テキストに変換せよ（参考: マークアップ早見表）．
"""

import re

def removeEmphasis(src):
    """入力から強調マークアップを除いて返す
    """
    result = re.subn("''+","",src)
    return result


if __name__ == "__main__":
    filepath = "03/data/britain.txt"
    with open(filepath,"r",encoding="utf-8")as file:
        text = file.read()

    template = {}

    regexp = "^\|(.*) = (.*(.|\n^(\*))*)"

    result = re.finditer(regexp,text,re.MULTILINE)

    for item in result:
        template[item.group(1)] = item.group(2) 

    ...
    #強調マークアップを削除
    for item in template:
        template[item] = removeEmphasis(template[item])

    print(template)