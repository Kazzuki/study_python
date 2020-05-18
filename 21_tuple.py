# リストの読み込み専用的なもの→追加や変更ができない
# タプルはカンマを付ける
# 対話型シェルで実行
t = (1,2,3,4,5)
type(t) #<class 'tuple'>

# t[0] = 3
# 下記の様にtupleに代入はできない
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# タプル内にリストを作り、そのリストの変更はできる
t =([2,3,4],[5,6,7])
t[0][0] = 1  #([1, 3, 4], [5, 6, 7])

t = 1,
type(t) #<class 'tuple'>
new_tuple = (1,2,3) + (4,5,6) #(1, 2, 3, 4, 5, 6)

#タプルのアンパッキング

num_tuple = (10,20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20 #Pythonではタプルの変数展開という意味になる(,がついているので)

#通常の数値の入れ替え

i = 20
j = 10
print('i=',i)
print('j=',j)

tmp = i
i = j
j =tmp

print('i=',i)
print('j=',j)

#タプルを用いた数値の入れ替え
a = 100
b = 200
print('a=',a)
print('b=',b)

a, b = b, a #入れ替えは一行で済む

print('a=',a)
print('b=',b)

# タプルの使い所(ex.変更すべきでない項目を並べる)
chose_from_two = ('a','b','c') #洗濯項目はタプル型なので変更できない（変更しようとするとエラーが発生する）
answer = []

answer.append('a')
answer.append('b')

print(chose_from_two)
print(answer)

