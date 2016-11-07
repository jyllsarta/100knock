# -*- coding: utf-8 -*-
"""40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは
表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，
3文目の形態素列を表示せよ．
"""

class Morph:
    """形態素のクラス
    """
    def __init__(self, src, **kwargs):
        """cabochaが標準で出力する形態素解析結果をsrcに与えると解釈する"""
        self.surface, rest = src.split("\t")
        misc = rest.split(",")
        self.base, self.pos, self.pos1 = misc[:3]
        self.orig = misc[-3]

        return super().__init__(**kwargs)

def readCaboChaFile(filepath):
    analysed_text = []
    sentence = []

    with open(filepath,"r",encoding="utf-8") as f:
        line = f.readline()
        while line:
            #EOSがあったら1行おわり
            if line == "EOS\n":
                analysed_text.append(sentence)
                sentence = []
            # "* "から始まる行は係り受け関係の表示
            elif line[:2] == "* ":
                ... #今は何もしない
            #それ以外は形態素
            else:
                sentence.append(Morph(line))
            line = f.readline()
    return analysed_text


if __name__ == "__main__":

    filepath = "05/data/neko.txt.cabocha"
    cabocha = readCaboChaFile(filepath)

    for m in cabocha[2]:
        print(m.surface, end="")