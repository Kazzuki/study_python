# 対話型シェルで実行
d = {'x':10, 'y':20}

d['x'] #10
d['y'] #20
d['x'] = 33 #{'x': 33, 'y': 20}
d['z'] = 999 #{'x': 33, 'y': 20, 'z': 999}
type(d) #<class 'dict'>
dict(a=10, b=20) #{'a': 10, 'b': 20}
# dictの中をtupleで表現できる
dict([('a',100),('b',200)]) #{'a': 100, 'b': 200}


d = {'x': 10, 'y': 20}
# keyの確認
d.keys() #dict_keys(['x', 'y'])
d.values() #dict_values([10, 20])
d2 = {'x': 1000, 'j': 500}
# update()でオーバーライドできる
d.update(d2) #{'x': 1000, 'y': 20, 'j': 500}
d.get('x') #1000

# d['z']
# 上記はエラーが発生する
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'z'
r = d.get('z')
type(r) #<class 'NoneType'>
d.clear() #{}

d = {'x': 10, 'y': 20}
'a' in d #False
'x' in d #True

# 辞書型も参照渡しになるのでコピーの際には気をつける

# 辞書型の使い所
# 辞書型はハッシュテーブルを用いるので、リスト型より検索が早くなる
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])