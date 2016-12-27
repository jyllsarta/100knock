# -*- coding: utf-8 -*-
"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""
#なんでKVSでこんなことするの？

import redis
import json


def constructDatabase(connection):
    """KVSにデータを投入する.(10分ほどかかります) connection:redisのコネクション"""

    r = connection

    print("Redisに何も積まれていないようです. DBを再構築しますか? (y/n)\n(93万件のレコードを挿入するため、この操作には10分ほどかかります)")
    if input() == "y":
        with open("07/data/artist.json",encoding="utf-8") as f:
            line = f.readline()
            while line:
                artist = json.loads(line)
                line = f.readline()

                if "name" in artist:
                    r.set(artist["name"],artist.get("area",""))

                counter += 1
                if counter % 20000 == 0:
                    print("{} 件投入しました.".format(counter))
            print("全件投入しました.")
    else:
        print("終了します.")
        exit()


if __name__ == "__main__":

    r = redis.Redis(host='localhost', port=6379, db=0)

    if r.dbsize() == 0:
        constructDatabase(r)

    count = 0
    Ncount = 0
    for i in r.scan_iter():
        if r.get(i.decode()).decode() == "Japan":
            count += 1
        Ncount += 1
        if Ncount % 10000 == 0:
            print("{}件スキャンしたよ.現状で日本で活動している人の数:{}".format(Ncount,count))

    print(count)    

