# -*- coding: utf-8 -*-
"""11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，
もしくはexpandコマンドを用いよ．
"""

import subprocess

#check_outputが改行文字で切れてしまうのでsedの出力全体を得られない...
#def replace_with_sed(content):
#    """sedコマンド経由で置換する
#    """
#    #OSコマンドインジェクション攻撃の対象になるよ
#    cmd = """echo {} | sed -e 's/"\t"/ /g' """.format(content)
#    ret = subprocess.check_output(cmd,shell=True).decode(encoding="utf-8")
#    print(ret)
#    return ret

if __name__ == "__main__":
    filepath = "data/hightemp.txt"

    with open(filepath,encoding="utf-8") as file:
        content = file.read()

    replaced = content.replace("\t"," ")

    #答え合わせは諦めた...
    #confirm = replace_with_sed(content)
    #is_OK = lambda x,y:"OK" if x==y else "NG"
    #output = "python:{}\nsed   :{}\n{}".format(replaced,confirm,is_OK(replaced,confirm))
    #print(output)

    print(replaced)


