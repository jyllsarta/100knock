# -*- coding: utf-8 -*-
"""10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import subprocess

def wc(filepath):
    """filenameを開いて行数を返す
    """
    i = 0;
    with open(filepath,encoding="utf-8") as file:
        while(file.readline()):
            i = i + 1;
    return i;

def exec_wc(filepath):
    """wcコマンド経由でファイルを開いて行数を返す
    """

    #OSコマンドインジェクション攻撃の対象になるよ
    cmd = "wc -l {}".format(filepath)

    ret = subprocess.check_output(cmd,shell=True).decode(encoding="utf-8")
    lines = int(ret.split(" ")[0])
    
    return lines

if __name__ == "__main__":
    filepath = "data/hightemp.txt"

    lines = wc(filepath)
    lines_exec = exec_wc(filepath)

    is_OK = lambda x,y:"OK" if x==y else "NG"

    output = "python:{}, wc command:{}, {}".format(lines,lines_exec,is_OK(lines,lines_exec))

    print(output)
