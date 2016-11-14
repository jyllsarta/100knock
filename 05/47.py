# -*- coding: utf-8 -*-
"""47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
    コーパス中で頻出する述語（サ変接続名詞+を+動詞）
    コーパス中で頻出する述語と助詞パターン
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

def extractCasePattern(sentence):
    """格パターンを抽出"""
    s = sentence
    casePatterns = []
    for i in range(len(s)):
        hasSahen = False
        morphs = s[i].morphs
        for j in range(1,len(morphs)):
            if morphs[j].surface == "を" and morphs[j-1].base == "名詞" and morphs[j-1].pos == "サ変接続":
                hasSahen = True
                targetnoun = morphs[j-1].surface
        if hasSahen and s[s[i].dst].hasVerb():
            firstVerb = s[s[i].dst].getFirstVerb()
            joshiList = []
            for src in s[s[i].dst].srcs:
                joshi = s[src].getLastJoshi()
                surface = s[src].toString()
                if joshi is not None and joshi != "を":
                    joshiList.append((joshi,surface))
            if len(joshiList) > 0:
                casePatterns.append((targetnoun+"を"+firstVerb,joshiList))
    return casePatterns

if __name__ == "__main__":

    filepath = "05/data/neko.txt.cabocha"
    cabocha = readCaboChaFile(filepath)


    with open("casepatterns.tsv","w",encoding="utf-8") as f:
        for line in cabocha:
            pattern = extractCasePattern(line)
            for p in pattern:
                f.write("{}\t{}\t{}\n".format(p[0]," ".join([x[0] for x in p[1]])," ".join([x[1] for x in p[1]])))




    