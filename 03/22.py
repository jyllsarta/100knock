# -*- coding: utf-8 -*-
"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
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