# -*- coding: utf-8 -*-
"""
"""

import re

def removeMarkup(src):
    """入力から強調/内部リンクマークアップを除いて返す
    """
    #強調を削除
    src = re.sub("''+","",src)

    #内部リンクを削除
    result = re.sub("\[\[.*?\|?(.+?)\]\]",lambda x:x.group(1),src)
    

    return result


if __name__ == "__main__":
    filepath = "03/data/britain.txt"
    with open(filepath,"r",encoding="utf-8")as file:
        text = file.read()

    template = {}

    #基礎情報テンプレート部分のみ抽出
    regexp = "^\|(.*) = (.*(.|\n^(\*))*)"
    result = re.finditer(regexp,text,re.MULTILINE)
    for item in result:
        template[item.group(1)] = item.group(2) 

    trimmed = {}
    #マークアップを削除
    for item in template:
        trimmed[item] = removeMarkup(template[item])

    print(trimmed)