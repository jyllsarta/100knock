# -*- coding: utf-8 -*-
"""09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は
残し，それ以外の文字の順序をランダムに並び替えるプログラムを
作成せよ．ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could 
actually understand what I was reading : the phenomenal 
power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

def randomizeLetter(word):
    """wordの順番を適当に並び替える
    """
    #なんかイケてない書き方で気になる
    listed = list(word)
    random.shuffle(listed)
    return "".join(listed)

def typoglycemia(text):
    """入力文の単語に対して最初と最後だけ残してそれ以外をランダマイズ
    「こんちには みさなん おんげき ですか」にする
    """
    typoglycem = []

    words = text.split(" ")
    for word in words:
        if len(word) <= 4:
            typoglycem.append(word)
        else:
            typo = lambda x:x[0] + randomizeLetter(x[1:-1]) + x[-1]
            typoglycem.append(typo(word))
    return " ".join(typoglycem)

if __name__ == "__main__":

    src = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(src))

    japanese = """こんにちは みなさん おげんき ですか？ わたしは げんき です。 
この ぶんしょう は いぎりす の ケンブリッジ だいがく の けんきゅう の けっか 
にんげん は もじ を にんしき する とき その さいしょ と さいご の もじさえ あっていれば  
じゅんばん は めちゃくちゃ でも ちゃんと よめる という けんきゅう に もとづいて 
わざと もじの じゅんばん を いれかえて あります。 
どうです？　ちゃんと よめちゃう でしょ？ 
ちゃんと よめたら はんのう よろしく """

    print(typoglycemia(japanese))
