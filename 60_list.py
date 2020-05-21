# リスト内包表記→可読性を損ねない程度のコードを書くこと
t = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)

# 悪い
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

# 良い(コードがスッキリ可読性も上がる)
r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)
# あまり良くない
r = [i * j for i in t for j in t2]
print(r)

# 辞書の内包表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 良い(コードがスッキリ可読性も上がる)
d = {x: y for x, y in zip(w, f)}
print(d)

# 集合の内包表記
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

# 良い(コードがスッキリ可読性も上がる)
s = {i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレーターの内包表記
def g():
    for i in range(10):
        yield i

g = g()
# gは<generator object g at 0x101c39f20>というオブジェクトを持つ
print(g)
# <class 'generator'>
print(type(g))
print(next(g))
print(next(g))
print(next(g))

#  良い(コードがスッキリ可読性も上がる)
#  ()→はジェネレーターの内包表記になる
g = (i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)

#tuple()→タプルの内包表記
t = tuple(i for i in range(10) if i % 2 == 0)
print(type(t))
print(t)
for x in g:
    print(x)