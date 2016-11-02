# -*- coding: utf-8 -*-
"""29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，
ファイル参照をURLに変換すればよい）
"""

import re
import requests
import urllib
import json

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


    flag_filename = trimmed["国旗画像"]

    #URlエンコードはもうちょっとしっかり調べたほうが良さそう...
    URL = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:{}&prop=imageinfo&format=json&iiprop=url".format(flag_filename).replace(" ","%20")

    resp = requests.get(URL)
    
    jsondata = json.loads(resp.text)

    #pageidの分離が必要ならあとでやる
    print(jsondata["query"]["pages"]["347935"]["imageinfo"][0]["url"])