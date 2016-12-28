# -*- coding: utf-8 -*-
"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）の
リストを検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，
アーティスト名からタグと被タグ数を検索せよ．
"""

import redis
import json

def constructDatabase(connection):
    """KVSにデータを投入する.(10分ほどかかります) connection:redisのコネクション"""

    r = connection
    counter = 0

    print("Redisに何も積まれていないようです. DBを再構築しますか? (y/n)\n(93万件のレコードをスキャン/挿入するため、この操作には10分ほどかかります)")
    if input() == "y":
        with open("07/data/artist.json",encoding="utf-8") as f:
            line = f.readline()
            while line:
                artist = json.loads(line)
                line = f.readline()

                if "name" in artist:
                    r.set(artist["name"],artist.get("tags",""))

                counter += 1
                if counter % 20000 == 0:
                    print("{} 件投入しました.".format(counter))
            print("全件投入しました.")
    else:
        print("終了します.")
        exit()


def flushDatabase(connection):
    """DBをリセットする"""
    r = connection
    r.flushall()

if __name__ == "__main__":

    r = redis.Redis(host='localhost', port=6379, db=0)

    if r.dbsize() == 0:
        constructDatabase(r)

    print(r.get("水樹奈々").decode())
