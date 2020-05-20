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