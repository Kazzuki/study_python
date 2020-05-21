# コマンドラインの引数が利用できる！
"""
import sys
print(sys.argv)

for w in sys.argv:
    print(w)
"""

#moduleの話
"""
・関数を読み込むんでなくて、moduleを経由して読み込むこと！(コンフリクトや関数の特定に困る)
・フルパスで読み込みなさい！っていうルールを持つ会社もある
・asをつかってしまうと、どんなモジュールかわからなくなる可能性もある！

"""

#その①_フルパスで書いてあげる(サードパーティや他のチームが開発したものでも区別がつく！)
"""
# pakage.moduleの関係（酒井先生はこう読んでいる）
import lesson_package.tool.utils
r = lesson_package.tool.utils.say_twice('kazuki')
print(r)
"""
#その②_module.メソッドで書いてあげる
"""
from lesson_package.tool import utils
r = utils.say_twice('kazuki')
print(r)
"""
#その③_asで書いてあげる(モジュール名がメチャクチャなときには有効)
"""
from lesson_package.tool import utils as hoge
r = hoge.say_twice('kazuki')
print(r)
"""

from lesson_package.talk import human
print(human.cry())
