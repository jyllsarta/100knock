# -*- coding: utf-8 -*-
"""35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

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

    dest = []
    for sentence in neko:
        rensetu_noun = []
        for word in sentence:
            if word["base"] =="名詞":
                rensetu_noun.append(word)
            else:
                if len(rensetu_noun) >= 2:
                    dest.append(rensetu_noun)
                rensetu_noun = []
        if len(rensetu_noun) >= 2:
            dest.append(rensetu_noun)
    print(dest)

