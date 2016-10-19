# -*- coding: utf-8 -*-
"""13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べた
テキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

if __name__ == "__main__":
    col1 = open("data/col1.txt","r",encoding="utf-8")
    col2 = open("data/col2.txt","r",encoding="utf-8")

    c1 = col1.readline()
    c2 = col2.readline()
    with open("data/merged.txt","w",encoding="utf-8") as file:
        while(c1):
            file.write("{}\t{}".format(c1.replace("\n",""),c2))
            c1 = col1.readline()
            c2 = col2.readline()
