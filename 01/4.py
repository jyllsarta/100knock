# -*- coding: utf-8 -*-
"""04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. 
Arthur King Can."という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への
連想配列（辞書型もしくはマップ型）を作成せよ．
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


def makeMaterialDictionary(words,monoletters):
    """wordsを2文字(monoletterindexに該当する番号なら1文字)
    切り出してkeyとし、元単語をvalueにした辞書を作成する
    """
    dest = {}

    for i in range(0,len(words)):
        if(i+1 in  monoletters):
            key = words[i][0]
        else:
            key = words[i][:2]
        dest[key] = words[i]
    return dest



if __name__ == "__main__":

    src = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    
    monoletterIndex = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    words = toWordList(src)

    materialDictionary = makeMaterialDictionary(words,monoletterIndex)

    print(materialDictionary)

    