# -*- coding: utf-8 -*-
"""49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiiとjj（i<ji<j）のとき，
係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現
（表層形の形態素列）を"->"で連結して表現する
文節iiとjjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iiから構文木の根に至る経路上に文節jjが存在する場合: 文節iiから文節jjのパスを表示
上記以外で，文節iiと文節jjから構文木の根に至る経路上で共通の文節kkで交わる場合:
 文節iiから文節kkに至る直前のパスと文節jjから文節kkに至る直前までのパス，文節kkの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
"""

import copy

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

    def toString(self,depressPunctuation=False,noun_to=None):
        """自身の形態素の表層形を読み上げて返す 
        depressPunctuationがTrueなら句読点は出力しない
        noun_toが何か入っていれば名詞はそれに置換
        """

        words = []
        for w in self.morphs:
            if depressPunctuation and w.base == "記号":
                continue
            if noun_to is not None and w.base == "名詞":
                words.append(noun_to)
                continue
            words.append(w.surface)
        return "".join(words)


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

    def isNounPhrase(self):
        """名詞句? (暫定的に名詞があれば名詞句とする)"""
        for m in self.morphs:
            if m.base == "名詞":
                return True
        return False

    def replaceNounTo(self,replaced):
        """自身の持つ名詞をreplacedに置換"""
        for w in self.morphs:
            if w.base == "名詞":
                w.surface = replaced



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

def findNounPhraseIndex(s,to):
    """sの文のto番目の文節以降の名詞句を探索"""
    phraseIndexs = []

    for i in range(to+1,len(s)):
        if s[i].isNounPhrase() : 
            phraseIndexs.append(i)
    return phraseIndexs

def toChankPathText(s,i,j):
    """文sのi番目の文節からj番目の文節のパスを返す"""

    #i -> j でまっすぐつながっている場合
    print("{},{}".format(i,j))
    dst = s[i].dst
    pathindex_i = [i]
    while dst != -1:
        pathindex_i.append(dst)
        if dst==j:
            #目的のパスが見つかったら早期returnでさっさと返す
            s[pathindex_i[0]].replaceNounTo("X")
            s[pathindex_i[-1]].replaceNounTo("Y")
            string = " -> ".join([s[idx].toString() for idx in pathindex_i])
            return string
        dst = s[dst].dst


    #i->k , j->k と途中で合流しているパターン
    dst = s[j].dst
    pathindex_j = [j]
    while dst != -1:
        pathindex_j.append(dst)
        dst = s[dst].dst
    
    for idx_i in range(len(pathindex_i)):
        for idx_j in range(len(pathindex_j)):
            #前から順に見ていって最初に見つかった共通の係り先
            if pathindex_i[idx_i] == pathindex_j[idx_j]:
                path_i = [s[idx] for idx in pathindex_i[:idx_i]]
                path_i[0].replaceNounTo("X")
                i_str = " -> ".join([m.toString() for m in path_i])

                path_j = [s[idx] for idx in pathindex_j[:idx_j]]
                path_j[0].replaceNounTo("Y")
                j_str = " -> ".join([m.toString() for m in path_j])

                formatted = "{} | {} | {}".format(i_str,j_str,s[s[pathindex_i[-1]].dst].toString(depressPunctuation=True))
                return formatted

if __name__ == "__main__":

    filepath = "05/data/neko.txt.cabocha"
    cabocha = readCaboChaFile(filepath)

    s = cabocha[7]

    chunkPaths = []

    for i in range(len(s)):
        if s[i].isNounPhrase():
            npIndex = findNounPhraseIndex(copy.deepcopy(s),i)
            print(npIndex)
            for j in npIndex:
                path = toChankPathText(copy.deepcopy(s),i,j)
                chunkPaths.append(path)
                print(path)

    for path in chunkPaths:
        print(path)



