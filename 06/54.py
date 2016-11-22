# -*- coding: utf-8 -*-
"""54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

import xml.etree.ElementTree as x

if __name__ == "__main__":
    filepath = "06/data/nlp.txt.xml"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        tree = x.fromstring(content)

    sentences = tree[0][0]

    for sentence in sentences:
        for token in sentence[0]:
            word = token.find("word").text
            lemma = token.find("lemma").text
            POS = token.find("POS").text
            print("\t".join((word,lemma,POS)))


