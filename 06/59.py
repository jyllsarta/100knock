# -*- coding: utf-8 -*-
"""59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
"""
import xml.etree.ElementTree as x
import json

def process(tree,token):
    """treeの☆を現在のプリンタのヘッダ位置と考えて、☆にtokenの要素に合わせた処理を施して返す"""

    #tokenがからの場合何もしない
    if token == "":
        return tree #parseオブジェクトがたまに空文字列入れてくるのでそのときには何もしない

    # ( の場合、リストの始まり
    # [word,☆] → [word,[☆]]
    if token == "(":
        return tree.replace('☆','[☆]')

    # ) の場合、直前の括弧を抜ける
    # [[word.☆]] → [[word],☆]
    if token == ")":
        tree = tree.replace(',☆','☆') 
        return tree.replace('☆]','],☆')

    #それ以外の場合、シンボルなので括弧内で並列する
    # [☆] → ["token",☆]
    else:
        return tree.replace('☆', '"'+token + '",☆')

def readTree(tree):
    """木構造に含まれている単語を探して読みあげて返す"""

    #ドット対なら終端なので読み上げる
    if type(tree[1]) is str:
        print(tree[1],end=" ")
        return

    #それ以外なら頭以外を同じ処理する
    for rest in tree[1:]:
        readTree(rest)

def findNP(tree):
    """再帰的にNPを探して返す"""

    #文字列まで来ていたら木の根っこまで掘ってきているのでおわり
    if type(tree) is str:
        return

    #今触っている木がNPなら木の枝の単語を全部読み上げてresultsetに追記する
    if tree[0] == "NP":
        for k in tree[1:]:
            readTree(k)
        print()

    #木構造の残りに対して同じ処理を行う
    for rest in tree[1:]:
        findNP(rest)

if __name__ == "__main__":
    filepath = "06/data/nlp.txt.xml"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        tree = x.fromstring(content)

    sentences = tree.find("document").find("sentences")

    sentence = sentences[4]

    S = sentence.find("parse").text

    #トークン単位で分割
    S = S.replace("\n          "," ")
    S = S.replace("(","( ")
    S = S.replace(")"," )")
    Slist = S.split(" ")

    
    #解析
    treeString = "☆"
    while Slist:
        token = Slist.pop(0)
        treeString = process(treeString,token)

    #解析終了後尻尾に ,☆ があるはずなので削除
    treeString = treeString[:-2]
    
    #大胆にjsonとして読み込む
    tr = json.loads(treeString)

    #NPを抽出
    findNP(tr)





