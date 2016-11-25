# -*- coding: utf-8 -*-
"""56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，
文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""

import xml.etree.ElementTree as x

def toStringSentence(sentence):
    """etreeのsentence要素をtextを連結して文にして返す"""
    return " ".join([x.find("word").text.replace("-LRB-", "(").replace("-RRB-", ")") for x in sentence.find("tokens").findall("token")])

if __name__ == "__main__":
    filepath = "06/data/nlp.txt.xml"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        tree = x.fromstring(content)

    sentences = tree.find("document").find("sentences").findall("sentence")
    refs = tree.find("document").find("coreference").findall("coreference")
    mentions = []

    #mentionをパース
    for ref in refs:
        mention = ref.find("mention")
        ref = {}
        ref["sentence"] = mention.find("sentence").text
        ref["start"] = mention.find("start").text
        ref["end"]   = mention.find("end").text
        ref["head"]  = mention.find("head").text
        ref["text"]  = mention.find("text").text
        mentions.append(ref)

    #パースしたmentionごとにetreeを書き換え
    for mention in mentions:
        sentenceId = int(mention["sentence"])-1  #リストは0オリジンなのでいっこずらす
        end = int(mention["end"]) -2 #2個ずれる
        head = int(mention["head"]) -1
        text = mention["text"]

        tokens = sentences[sentenceId].find("tokens")
        tokens[head].find("word").text = " <<{}>> ({}".format(text,tokens[head].find("word").text)
        tokens[end].find("word").text = "{}) ".format(tokens[end].find("word").text)
        
    #画面に表示
    for sentence in sentences:
        print(toStringSentence(sentence))


