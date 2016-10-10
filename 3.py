# -*- coding: utf-8 -*-

def getLengthList(iterables):
    """iterableを受け取り各要素のlengthを返す
    """
    lenList = []
    for it in iterables:
        lenList.append(len(it))
    return lenList

def removePunctuation(text):
    """textからコンマとピリオドを取り除いて返す
    """
    removed = []
    for letter in text:
        if letter == "," or letter == ".":
            continue
        removed.append(letter)
    return "".join(removed)

def toWordList(text):
    """入力を単語ごとに区切ってリストにして返す
    """
    return removePunctuation(text).split(" ")

if __name__ == "__main__":
    """03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """

    src = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    words = toWordList(src)

    wordLengthList = getLengthList(words)

    print(wordLengthList)

