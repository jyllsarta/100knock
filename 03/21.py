# -*- coding: utf-8 -*-
"""21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import re

if __name__ == "__main__":
    filepath = "03/data/britain.txt"
    with open(filepath,"r",encoding="utf-8")as file:
        raw = file.read()

    article = raw.split("\n")
    category = []
    for line in article:
        match = re.match("\[\[Category:(.+?)(\|.+?)??\]\]",line)
        if match:
           category.append(match.group(1))

    print(category)