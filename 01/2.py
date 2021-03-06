# -*- coding: utf-8 -*-
"""02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して
文字列「パタトクカシーー」を得よ．
"""

def conbine(a,b):
    """aとbを交互に連結した文字列を返す
    len(a) == len(b)前提です
    """

    dest = [];
    for i in range(0,len(b)):
        dest.append(a[i])
        dest.append(b[i])
    return "".join(dest)

if __name__ == "__main__":

    patcar = "パトカー"
    taxi = "タクシー"

    print(conbine(patcar,taxi))
