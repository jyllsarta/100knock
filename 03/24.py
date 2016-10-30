# -*- coding: utf-8 -*-
"""24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""


import re

if __name__ == "__main__":
    filepath = "03/data/britain.txt"
    with open(filepath,"r",encoding="utf-8")as file:
        raw = file.read()

    article = raw.split("\n")
    files = []

    regexp = "\[\[File:(.+?)(\|.+?)"

    for line in article:
        match = re.match(regexp,line)
        if match:
           files.append(match.group(1))

    #なんかあっさり終わりすぎてこれで完全に拾えているか心配になるね
    for file in files:
        print(file)