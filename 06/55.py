# -*- coding: utf-8 -*-
"""55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""

import xml.etree.ElementTree as x

def getPersonName(sentence):
    """文から人名を抜き出して集合を返す"""
    name = set()
    name_flagment = []
    for token in sentence:
        if token.find("NER").text == "PERSON":
            name_flagment.append(token.find("word").text)
        elif name_flagment != []:
            #今の単語が人名でなく、直前が人名だった = 人名はここで終わり
            name.add(" ".join(name_flagment))
            name_flagment = []
    if name_flagment != []:
        #今の単語が人名でなく、直前が人名だった = 人名はここで終わり
        name.add(" ".join(name_flagment))
        name_flagment = []

    if len(name) == 0:
        return None
    else:
        return name

if __name__ == "__main__":
    filepath = "06/data/nlp.txt.xml"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        tree = x.fromstring(content)

    sentences = tree[0][0]
    names = set()

    for sentence in sentences:
        tk = sentence.find("tokens")
        name = getPersonName(tk)
        if name is not None:
            names.update(name)

    print(names)

