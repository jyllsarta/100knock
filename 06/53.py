# -*- coding: utf-8 -*-
"""53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
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
            word = token[0]
            print(word.text)


