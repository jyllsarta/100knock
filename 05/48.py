# -*- coding: utf-8 -*-
"""48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，
その文節から構文木の根に至るパスを抽出せよ． 
ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文
（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
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

    def toString(self,depressPunctuation=False):
        """自身の形態素の表層形を読み上げて返す depressPunctuationがTrueなら句読点は出力しない"""
        if depressPunctuation:
            return "".join([m.surface for m in self.morphs if m.base != "記号"])
        else:
            return "".join([m.surface for m in self.morphs])

    def hasNoun(self):
        """名詞を持つ?"""
        return (True in [m.base == "名詞" for m in self.morphs])

    def hasVerb(self):
        """動詞を持つ?"""
        return (True in [m.base == "動詞" for m in self.morphs])

    def getFirstVerb(self):
        """最初の同士の基本形を返す"""
        for m in self.morphs:
            if m.base == "動詞":
                return m.orig
        print("動詞なかったよ? chunk={}".format(self.toString()))
        return ""

    def getLastJoshi(self):
        """最後の助詞を返す"""
        for m in self.morphs[::-1]:
            if m.base == "助詞":
                return m.surface
        #print("助詞なかったよ? chunk={}".format(self.toString()))
        return None


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

def getChunkPath(s,c):
    """文sにおいて文節cのかかり順どおりに繋がったリストを返す"""
    path = []
    chunk = c
    path.append(chunk)
    while chunk.dst != -1:
        chunk = s[chunk.dst]
        path.append(chunk)
    return path

if __name__ == "__main__":

    filepath = "05/data/neko.txt.cabocha"
    cabocha = readCaboChaFile(filepath)

    s = cabocha[7]

    chunkPaths = []
    for c in s:
        chunkPaths.append(getChunkPath(s,c))

    for path in chunkPaths:
        print(" -> ".join([x.toString(depressPunctuation=True) for x in path]))



