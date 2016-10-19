# -*- coding: utf-8 -*-
"""12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""

if __name__ == "__main__":
    filepath = "data/hightemp.txt"

    col1 = []
    col2 = []

    with open(filepath,encoding="utf-8") as file:
        line = file.readline()
        while(line):
            c1,c2 = line.split("\t")[:2]
            col1.append(c1)
            col2.append(c2)
            line = file.readline()

    with open("data/col1.txt","w",encoding="utf-8") as col1_file:
        for item in col1:
            col1_file.write(item + "\n")

    with open("data/col2.txt","w",encoding="utf-8") as col2_file:
        for item in col2:
            col2_file.write(item + "\n")










