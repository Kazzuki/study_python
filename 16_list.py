
#文字列は挿入ができなかったが、listは挿入ができる
l = [1,2,3,5,69,489]
l[0] #1
type(l) #<class 'list'>
l[::2] #[1, 3, 69]
l[::-1] #[489, 69, 5, 3, 2, 1]

#ネスト
a = ['a','b','c']
m = [2,3,4]
g = [a,m] #[['a', 'b', 'c'], [2, 3, 4]]
g[0] #['a', 'b', 'c']
g[0][2] #'c'

n=[1, 2, 3, 4, 4, 4, 4, 4, 4, 9, 10]
n[3]=100 #[1, 2, 3, 100, 4, 4, 4, 4, 4, 9, 10]
n.append(999) #[1, 2, 3, 100, 4, 4, 4, 4, 4, 9, 10, 999]
n.insert(0,888) #[888, 1, 2, 3, 100, 4, 4, 4, 4, 4, 9, 10, 999]
n.insert(5,888) #[888, 1, 2, 3, 100, 888, 4, 4, 4, 4, 4, 9, 10, 999]
n.pop() #999 n=[888, 1, 2, 3, 100, 888, 4, 4, 4, 4, 4, 9, 10]
n.pop(0) #888 n=[1, 2, 3, 100, 888, 4, 4, 4, 4, 4, 9, 10]

del n[0]
del n #list nごと消える

n = [1,2,3,4,5]
n.remove(2) #[1, 3, 4, 5]

a = [1,2,3,4,5]
b = [6,7,8,9,10]

a += b #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x=[6,7,8,9,10]
y=[1,2,3,4,5]
y.extend(x) #y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = [1,2,3,4,5,1,2,3]
print(r.index(3)) # 2
print(r.index(3,3)) #r[3]から3を探し始める→ # 7
print(r.count(5)) #5はrの中に何個あるのかカウントする

if 5 in r:
    print('r has 5')

if 100 in r:
    print('r has 100')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Kazuki.'
to_split = s.split(' ')
print(to_split)

x = '***'.join(to_split) #listを***でつなぐ
print(x)

# print(help(list)) → listの使い方が参照できる

# 値渡し　→　数字に場合は値渡し、オブジェクトのidが異なる
# 参照渡し　→リストやディクショナリは参照渡しになる(他の言語だと明示的にポインタだと表すが、pythonはそれをしなくていいため、バグになる可能性を理解しておく)、オブジェクトのidが同じになる
i =[1, 2, 3, 4, 5]
j = i
y[0] = 100
print('i =',i)
print('j =',j)

x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]
y[0] = 100
print('x =',x)
print('y =',y)

# objectのidを確認してみる
# 値渡し
x = 20
y = x
y = 5
print('x =',id(x))
print('y =',id(y))
print('x =',x)
print('y =',y)

# 参照渡し
x = ['a', 'b']
y = x
y[0] = 'q'
print('x =',id(x))
print('y =',id(y))
print('x =',x)
print('y =',y)

#リストの使い所(ex.タクシーの座席状況をリストで表現してみる)
#対話型シェルで実行
seat = []
min = 0
max = 5
min <= len(seat) < max
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
min <= len(seat) < max #True
seat.append('p')
min <= len(seat) < max #False
len(seat) #5
seat.pop()
min <= len(seat) < max #True