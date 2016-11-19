# -*- coding: utf-8 -*-
"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．
"""

import re

if __name__ == "__main__":

    filepath = "06/data/nlp.txt"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        replaced = re.sub("([\.;:\?\!]) ([A-Z])","\1 \n\2",content)

    print(replaced)