# 組み込み関数→buildins(importしなくても使える関数のこと) 
# https://docs.python.org/ja/3.6/library/functions.html

# import builtins
# builtins.print('hogehoge')
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking,key=ranking.get, reverse=True))

# 標準ライブラリはimportして使う必要がある

s = "ajsdfljasgawseurtajhsdljfkalhsdgglsdjrrwetfalksjdglaugaojwelgrjadtle"

# ①s内のアルファベットを種類別にカウントする
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)
# ②
d = {}
for c in s:
    # setdefaultに置き換えれる
    d.setdefault(c, 0)
    d[c] += 1
print(d)

# ③
# 標準ライブラリをimportする
# https://docs.python.org/ja/3.6/library/collections.html
from collections import defaultdict
d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

#(★) サードパーティ→その対象となっている製品自体の開発元・販売元ではない企業のこと
# サードパーティ(第三者が作った)のライブラリを使う
#PyPI(Python Package Index)は、プログラミング言語Pythonの、サードパーティーソフトウェアリポジトリ
# pip install 〇〇でサードパーティを持って来れる(外部からパッケージをインストールするやり方)

from termcolor import colored

print('test')

print(colored('test','green'))
print(colored('test',on_color='on_green'))
# print(help(colored))

# (★)【超重要！！】
# サードパーティのパッケージはsite-packagesにinstallされる
# 標準ライブラリはpython3.6の真下にいる
# ローカルのパッケージがはじめに呼び出されるので、同じ名前にはしないこと！

# 標準ライブラリ
import collections
import os
import sys
# サードパーティのライブラリ
import termcolor
# 他のチームが作ったライブラリ
import lesson_package
# 自分のライブラリ
import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(config.hello())

# sys.pathにかかれている順位pythonはパッケージを読み込むので,指定外にパッケージがいる場合は読み込まれない！
print('sys.pathの表示')
for path in sys.path:
    print(path)