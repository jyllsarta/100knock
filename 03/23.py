# -*- coding: utf-8 -*-
"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re

if __name__ == "__main__":
    filepath = "03/data/britain.txt"
    with open(filepath,"r",encoding="utf-8")as file:
        raw = file.read()

    article = raw.split("\n")
    section = []

    for line in article:
        match = re.match("(=+)(.*?)=+",line)
        if match:
           section.append((match.group(2),len(match.group(1))-1))

    for title in section:
        depth = title[1]
        str = title[0]
        #深さに応じてインデントして表示
        print("{}{}".format((lambda x:"  "*(x-1))(depth),str))

