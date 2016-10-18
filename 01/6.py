# -*- coding: utf-8 -*-
"""06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの
集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，
差集合を求めよ．さらに，'se'というbi-gramが
XおよびYに含まれるかどうかを調べよ．
"""

def toNgram(iterable,N):
    """iterableをN-Gramのリストにして返す
    """
    dest = []

    for i in (range(N,len(iterable)+1)):
        dest.append(iterable[i-N:i])

    return dest

if __name__ == "__main__":

    parapara = "paraparaparadise"
    paragura = "paragraph"
    keyword  = "se"

    X = set(toNgram(parapara,2))
    Y = set(toNgram(paragura,2))

    joinedSet = X.union(Y)
    productSet = X.intersection(Y)
    XDiffY = X.symmetric_difference(Y)
    YDiffX = Y.symmetric_difference(X)

    hasKeywordX = keyword in X
    hasKeywordY = keyword in Y

    print("X:")
    print(X)
    print("Y:")
    print(Y)
    print("X+Y:")
    print(joinedSet)
    print("X^Y:")
    print(productSet)
    print("X-Y:")
    print(XDiffY)
    print("Y-X:")
    print(YDiffX)
    print("Is there '"+keyword+"' in X?:")
    print(hasKeywordX)
    print("Is there '"+keyword+"' in Y?:")
    print(hasKeywordY)