# -*- coding: utf-8 -*-
"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち
末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．"""



import sys

if __name__ == "__main__":

    try:
        raw = sys.argv[1]
        N = int(raw)
    except ValueError:
        print("argument was not Number : {}".format(raw))
        exit()

    for i in range(0,N):
        print(input())
        #bash on windowsだと出力先をasciiだと思ってunicodedecodeerrorを吐く 他の環境だとうまくいく