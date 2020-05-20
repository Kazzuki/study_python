# よく使うメソッドは(★)
# iteratorがないとカウントを増やしていく処理を書く必要がある
"""
num_list = [1,2,3,4,5]
count = 0
while count < len(num_list):
    print(num_list[count])
    count += 1
"""
# イテレータ(Iterator) →  反復処理を繰り返すもの
# forを使うとiteratorが使える用いる(iにリストの先頭から要素がはいる。厳密には違うかも。。)
"""
num_list = [1,2,3,4,5]
for i in num_list:
    print(i)

for s in 'abcdefg':
    print(s)

for word in ['My', 'name', 'is', 'kazuki']:
    if word == 'name':
        break
    print(word)
"""

# for else文
"""
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        # elseを実行せずにループから抜ける
        break
    print(fruit)
else:
    print('I ate all!')
"""
# range関数(★)
# 第1引数→開始番号、第2引数→終了番号、第3引数→飛ばし方

# for i in range(2,10,2):
#     print(i)

# _はループ内で使われないインデックスであることを始めに明示できる
"""
for _ in range(10):
    print('hello')
"""
# enumerate関数→インデックスを用意してくれる
"""
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
"""
# zip関数→インデックを用意せず複数のリストを表示できる
# 最小単位にまとめて表示される
days = ['Mon', 'Tue', 'Wed', 'hoge']
fruits = ['apple', 'banana']
drinks = ['coffee', 'tea', 'beer', 'hoge']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

"""
for day, fruit, drink in zip(days, fruits, drinks):
    print(day,fruit,drink)
"""

# 辞書型をforで処理する(d.items())
d = {'x': 100, 'y': 200}

# keyだけ表示される
for k in d:
    print(k)
#d.itemsは何を返すのか？
print(d.items()) #([('x', 100), ('y', 200)])

#タプルをアンパッキングで展開する
for k, v in d.items():
    print(k,':', v)
