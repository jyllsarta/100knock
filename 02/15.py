# -*- coding: utf-8 -*-
"""15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys

if __name__ == "__main__":

    try:
        raw = sys.argv[1]
        N = int(raw)
    except ValueError:
        print("argument was not Number : {}".format(raw))
        exit()

    output_buffer = []

    for line in sys.stdin:
        output_buffer.append(line)

        #N個以上の行が溜まったら頭から捨てていく
        if len(output_buffer) > N:
            output_buffer.pop(0)

    for i in output_buffer:
        print(i,end="")