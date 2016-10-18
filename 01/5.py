# -*- coding: utf-8 -*-
"""05. n-gram
与えられたシーケンス（文字列やリストなど）から
n-gramを作る関数を作成せよ．この関数を用い，
"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

def removePunctuation(text):
    """textからコンマとピリオドを取り除いて返す
    """
    removed = []
    for letter in text:
        if letter == "," or letter == ".":
            continue
        removed.append(letter)
    return "".join(removed)

def toWordList(text):
    """入力を単語ごとに区切ってリストにして返す
    """
    return removePunctuation(text).split(" ")

def toNgram(iterable,N):
    """iterableをN-Gramのリストにして返す
    """
    dest = []

    for i in (range(N,len(iterable)+1)):
        dest.append(iterable[i-N:i])

    return dest

if __name__ == "__main__":

    src = "I am an NLPer"

    letterNgram = toNgram(src,2)
    wordNgram = toNgram(toWordList(src),2)

    print(letterNgram)
    print(wordNgram)
