# -*- coding: utf-8 -*-
"""41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）を
メンバ変数に持つこととする．さらに，
入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，8文目の文節の
文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

class Morph:
    """形態素"""
    def __init__(self, src, **kwargs):
        """cabochaが標準で出力する形態素解析結果をsrcに与えると解釈する"""
        self.surface, rest = src.split("\t")
        misc = rest.split(",")
        self.base, self.pos, self.pos1 = misc[:3]
        self.orig = misc[-3]

        return super().__init__(**kwargs)

class Chunk:
    """文節"""
    def __init__(self, dst, **kwargs):
        """dst : 係り先"""

        self.morphs = []
        self.dst = dst
        self.srcs = []
        return super().__init__(**kwargs)

    def addMorph(self, morph):
        self.morphs.append(morph)

    def addSource(self, src):
        self.srcs.append(src)

def fillSourceList(s):
    """sの文節ごとのかかり先を埋める"""
    for idx,chunk in enumerate(s):
        dst = s[idx].dst 
        if dst == -1:
            continue
        s[dst].addSource(idx)

def readCaboChaFile(filepath):
    text = []
    sentence = []
    chunk = None

    with open(filepath,"r",encoding="utf-8") as f:
        line = f.readline()
        while line:
            #EOSがあったら1行おわり
            if line == "EOS\n":
                if chunk is not None:
                    sentence.append(chunk)
                fillSourceList(sentence)
                text.append(sentence)
                sentence = []
                chunk = None
            # "* "から始まる行は係り受け関係の表示 
            # →新しい文節のスタート
            elif line[:2] == "* ":
                if chunk is not None:
                    sentence.append(chunk)

                #新しいものにする
                item = line.split(" ")
                dst = int(item[2][:-1]) #"13D" → 13
                chunk = Chunk(dst)
            #それ以外は形態素なので現在の文節に追加
            else:
                chunk.addMorph(Morph(line))
            line = f.readline()
    return text


if __name__ == "__main__":

    filepath = "05/data/neko.txt.cabocha"
    cabocha = readCaboChaFile(filepath)

    for i,c in enumerate(cabocha[7]):
        print("{}(to {}): ".format(i,(lambda x:x if x!=-1 else "x")(c.dst)) ,end="")
        for m in c.morphs:
            print(m.surface, end="")
        print()
