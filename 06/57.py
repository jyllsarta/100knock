# -*- coding: utf-8 -*-
"""57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を
有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，
Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，
pydotを使うとよい．
"""

import xml.etree.ElementTree as x
import graphviz


def getDepencencies(sentence):
    """文から係り受け関係を取得"""
    tokens = sentence.find("tokens")
    dependencies = sentence.find("dependencies[@type='collapsed-dependencies']")

    deps = []
    tks  = []

    for dep in dependencies:
        item = {}
        item["src_idx"]  = dep.find("governor").attrib["idx"]
        item["src_name"] = dep.find("governor").text

        item["dest_idx"]  = dep.find("dependent").attrib["idx"]
        item["dest_name"] = dep.find("dependent").text
        deps.append(item)

    deps_collection.append(deps)

    for token in tokens:
        tk = {}
        tk["idx"]  = token.attrib["id"]
        tk["text"] = token.find("word").text
        tks.append(tk)

    return deps,tks


if __name__ == "__main__":
    filepath = "06/data/nlp.txt.xml"
    with open(filepath,"r",encoding="utf-8") as f:
        content = f.read()
        tree = x.fromstring(content)

    sentences = tree.find("document").find("sentences")

    deps_collection = []

    sentence = sentences[1]    

    edges,vertice = getDepencencies(sentence)

    dot = graphviz.Digraph()

    for vertex in vertice:
        dot.node(vertex["idx"],vertex["text"])

    for edge in edges:
        dot.edge(edge["src_idx"], edge["dest_idx"])
        
    print(dot)