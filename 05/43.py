# -*- coding: utf-8 -*-
"""42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストを
タブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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

    #表示したい文を選択
    s = cabocha[11]

    for i in range(len(s)):
        if s[i].hasNoun() and s[s[i].dst].hasVerb():
            print("{} -> {}".format(s[i].toString(depressPunctuation=True),s[s[i].dst].toString(depressPunctuation=True)))