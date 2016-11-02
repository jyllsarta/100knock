# -*- coding: utf-8 -*-
"""28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値から
MediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．
"""

import re

def removeMarkup(src):
    """入力から強調/内部リンクマークアップを除いて返す
    """
    #強調を削除
    text = re.sub("''+","",src)

    #内部リンクを削除
    text = re.sub("\[\[.*?\|?(.+?)\]\]",lambda x:x.group(1),text)

    #{{lang|**|ほげ}}を削除
    text = re.sub("{{lang\|..\|(.*?)}}",lambda x:x.group(1),text)

    #<ref />を削除
    text = re.sub("<ref .*?/>","",text)

    #<ref>.*</ref>を削除
    text = re.sub("<ref.*?>.*?</ref>","",text)
    

    return text


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