# -*- coding: utf-8 -*-
"""58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
"""

import xml.etree.ElementTree as x
import graphviz


def getSVO(sentence):
    """主語、述語、目的語を抽出"""
    dependencies = sentence.find("dependencies[@type='collapsed-dependencies']")

    nsubj = dependencies.findall("dep[@type='nsubj']")
    dobj  = dependencies.findall("dep[@type='dobj']")


    gove = lambda x:x.find("governor").text
    depa = lambda x:x.find("dependent").text

    answer = []

    for ns in nsubj:
        for db in dobj:
           if gove(ns) == gove(db):
                answer.append((depa(ns), gove(ns), depa(db)))
    return answer

    #shugo = set([x.find("governor").text for x in nsubj]) & set([x.find("governor").text for x in dobj])


if __name__ == "__main__":
    filepath = "06/data/nlp.txt.xml"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        tree = x.fromstring(content)

    sentences = tree.find("document").find("sentences")

    sentence = sentences[4]


    for s in sentences:
        SVO = getSVO(s)
        for tup in SVO:
            print("\t".join(tup))