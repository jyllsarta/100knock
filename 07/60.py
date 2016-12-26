# -*- coding: utf-8 -*-
"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から
活動場所（area）を検索するためのデータベースを構築せよ．
"""

import redis
import json

if __name__ == "__main__":

    r = redis.Redis(host='localhost', port=6379, db=0)

    counter = 0
    with open("07/data/artist.json",encoding="utf-8") as f:
        line = f.readline()
        while line:
            artist = json.loads(line)
            line = f.readline()

            if "name" in artist:
                r.set(artist["name"],artist.get("area",""))

            counter += 1
            if counter % 100000 == 0:
                print("{} 件投入しました.".format(counter))
        print("おしまい")
    

