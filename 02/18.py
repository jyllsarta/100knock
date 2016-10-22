# -*- coding: utf-8 -*-
"""18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．
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

    print( sorted(content, key=lambda x:x[2], reverse=True))