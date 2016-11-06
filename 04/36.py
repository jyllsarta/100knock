# -*- coding: utf-8 -*-
"""36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import collections 

def toKeitaisoMap(line):
    """形態素解析結果テキストを1行取りマップを作成する
    """
    map = {}
    map["surface"],rest = line.split("\t")
    misc = rest.split(",")
    map["base"], map["pos"], map["pos1"] = misc[:3]
    map["orig"] = misc[-3]

    return map

def readMecabFile(filepath):
    analysed_text = []
    sentence = []

    with open(filepath,"r",encoding="utf-8") as f:
        line = f.readline()
        while line:
            if line == "EOS\n":
                analysed_text.append(sentence)
                sentence = []
            else:
                keitaiso_map = toKeitaisoMap(line)
                sentence.append(keitaiso_map)
            line = f.readline()
    return analysed_text

if __name__ == "__main__":
    filepath = "04/data/neko.txt.mecab"
    neko = readMecabFile(filepath)

    dest = collections.defaultdict(lambda :0)

    for sentence in neko:
        for word in sentence:
            dest[word["surface"]] = dest[word["surface"]] + 1 

    print(dest)

