# -*- coding: utf-8 -*-
"""17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""


if __name__ == "__main__":
    filepath = "02/data/hightemp.txt"

    col1 = set()

    with open(filepath,encoding="utf-8") as file:
        line = file.readline()
        while(line):
            c1 = line.split("\t")[0]
            col1.add(c1)
            line = file.readline()

    print(col1)

