# -*- coding: utf-8 -*-
"""30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを
実装せよ．ただし，各形態素は表層形（surface），
基本形（base），品詞（pos），品詞細分類1（pos1）をキーとする
マッピング型に格納し，1文を形態素（マッピング型）の
リストとして表現せよ．第4章の残りの問題では，
ここで作ったプログラムを活用せよ．
"""

def toKeitaisoMap(line):
    """形態素解析結果テキストを1行取りマップを作成する
    """
    map = {}
    map["surface"],rest = line.split("\t")
    map["base"], map["pos"], map["pos1"] = rest.split(",")[:3]
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

    print(neko)



