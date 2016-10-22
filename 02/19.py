# -*- coding: utf-8 -*-
"""19. 各行の1コラム目の文字列の出現頻度を求め，
出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，
その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""

import sys

if __name__ == "__main__":
    filepath = "02/data/hightemp.txt"

    
    content = []
    with open(filepath,encoding="utf-8") as file:
        line = file.readline()
        while line:
            content.append(line.split("\t"))
            line = file.readline()

    freq = {}
    for item in content:
        freq[item[0]] = freq.get(item[0],0) + 1

    sorted = sorted(list(freq.items()),key=lambda x:x[1],reverse=True)
    print(sorted)