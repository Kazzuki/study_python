a = {1,2,2,3,4,5,5,6,} #{1, 2, 3, 4, 5, 6}
type(a) #<class 'set'>
b = {1,4,5} #{1, 4, 5}
c = {'a','d','d'} #{'a', 'd'}
a & c #set()
a & b #{1, 4, 5}
a - b #{2, 3, 6}
a | b #{1, 2, 3, 4, 5, 6}
a ^ b #{2, 3, 6}


s = {1,2,3,4,5}
s.add(4) #{1, 2, 3, 4, 5}

#集合に並びの概念はないのでエラーが発生する
# s[2]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable

s.remove(5) #{1, 2, 3, 4}
s.clear() #set()


# リスト(追加していく箱)の中からユニークなもの(種類にまとめる)を取り出したい
my_friends = {'A', 'B', 'C'}
A_friends = {'B','K','D'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) #リストから型変換を行って集合型にしている
print(kind)