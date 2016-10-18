# -*- coding: utf-8 -*-
"""08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数
cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(text):

    crypted = []

    for letter in text:
        if ord("a") <= ord(letter) <= ord("z"):
            alter = lambda x:chr(219-ord(x))
            crypted.append(alter(letter))
        else:
            crypted.append(letter)

    return "".join(crypted)

if __name__ == "__main__":

    src = "a quick brown fox jumps over the lazy dog."

    print("元テキスト:")
    print(src)
    print("cipher:")
    print(cipher(src))
    print("cipher(ciphered):")
    print(cipher(cipher(src)))


