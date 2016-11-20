# -*- coding: utf-8 -*-
"""51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，
1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""

import re

if __name__ == "__main__":

    filepath = "06/data/nlp.txt"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        sentence_per_line = re.sub("([\.;:\?\!]) ([A-Z])","\1 \n\2",content)

    word_per_line = sentence_per_line.replace(" ","\n")
    print(word_per_line)