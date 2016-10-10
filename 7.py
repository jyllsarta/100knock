# -*- coding: utf-8 -*-


def makeFormattedText(when,what,how):
    """  returns "when時のwhatはhow"
    """
    return "{}時の{}は{}".format(when,what,how)

if __name__ == "__main__":
    """07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    """

    print(makeFormattedText(12,"気温",22.4))