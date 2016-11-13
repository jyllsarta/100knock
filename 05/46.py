# -*- coding: utf-8 -*-
"""46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）
をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． 
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
始める  で
見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン
（コーパス中で出現頻度の高い順に並べよ）
"""

import pydot

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
        print("助詞なかったよ? chunk={}".format(self.toString()))
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

def extractCasePattern(sentence):
    """格パターンを抽出"""
    s = sentence
    casePatterns = []
    for i in range(len(s)):
        if s[i].hasVerb():
            firstVerb = s[i].getFirstVerb()
            joshiList = []
            for src in s[i].srcs:
                joshi = s[src].getLastJoshi()
                surface = s[src].toString()
                if joshi is not None:
                    joshiList.append((joshi,surface))
            if len(joshiList) > 0:
                casePatterns.append((firstVerb,joshiList))
    return casePatterns

if __name__ == "__main__":

    filepath = "05/data/neko.txt.cabocha"
    cabocha = readCaboChaFile(filepath)

    #表示したい文を選択
    s = cabocha[7]
    pt = extractCasePattern(s)
    for p in pt:
        print("{}\t{}\t{}".format(p[0]," ".join([x[0] for x in p[1]])," ".join([x[1] for x in p[1]])))




    