# -*- coding: utf-8 -*-
"""34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
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
        if len(sentence) < 3:
            continue
        for w1,w2,w3 in zip(sentence,sentence[1:],sentence[2:]):
            #名詞 の 名詞 なら:
            if w1["base"]=="名詞" and w2["surface"]=="の" and w3["base"]=="名詞":
                dest.append(w1["surface"] + w2["surface"] + w3["surface"])

    print(dest)

