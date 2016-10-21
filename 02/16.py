# -*- coding: utf-8 -*-
"""16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import sys
import math

if __name__ == "__main__":
    try:
        raw = sys.argv[1]
        N = int(raw)
    except ValueError:
        print("argument was not Number : {}".format(raw))
        exit()

    inputfile = sys.stdin.readlines()

    size = len(inputfile) // N

    for i in range(N-1):
        #N-1分割目までは 入力行数 // N 行書き込む
        with open("data/split_{}.txt".format(i),"w",encoding="utf-8") as file:
            for line in inputfile[i*size:(i+1)*size]:
                file.write(line)
    #最後の一つにはあまりをすべて書き込む
    with open("data/split_{}.txt".format(i+1),"w",encoding="utf-8") as file:
        for line in inputfile[(i+1)*size:]:
            file.write(line)