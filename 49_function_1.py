#num: int = 10

#3.6では変数の型はintを想定していますよ！ぐらいの拘束力
def add_num(a: int, b: int) -> int:
    return a + b
# 実際にstringを引数として渡してもPythonはエラーをはかない
r = add_num('a','b')
print(r)

# 位置引数、キーワード引数、デフォルト引数

def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

menu('chicken', drink='beer')

# Pythonでは空の参照渡しを行うもの(リスト型、辞書型)をデフォルト引数で与えるべきでない
# 悪い例
"""
def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r) 
#2回目で[100, 100]となり、バグにつながる

"""
# 良い例
# 空の参照渡しを行うもの(リスト型、辞書型)を用いる場合は関数内のはじめに新たに定義する
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

y = [2,3,4,5]
r = test_func(100,y)
print(r)

r = test_func(100)
print(r) 

# (★)
# 位置引数のタプル化
# 悪い例→引数が長くなる
"""
def say_something(word, word1, word2):
    print(word)
    print(word1)
    print(word2)

say_something('Hi!','kauzki','hoge')
"""
# 良い例→タプルを用いて第2引数以降をタプル化する(可変長の引引数が用意できる)

# 展開されて渡された*tはもう一度タプル化されて関数内ではタプルとして利用できる
def say_something(word, *args):
    print(word)
    for word in args:
        print(word)

say_something('Hi!','kauzki','hoge')

t = ('hoge', 'hoge')
# (?)
say_something('kauzki', t)
"""
kauzki
('hoge', 'hoge')
"""
# (?)
# *によってタプルを展開して渡される。
say_something('kauzki', *t)
"""
kauzki
hoge
hoge
"""

say_something(*t)

