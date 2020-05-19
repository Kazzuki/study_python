# Pythonはインデントを無理やり合わせないとエラーが発生する


x = 10
# ifのあとは4つのインデントを入れることが推奨される
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
# 上から順にcodeを実行している原則を忘れずに！
elif x == 10:
    print('1000000000')
elif x == 10:
    print('10')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

# 比較演算子と論理演算子
a = 1
b = 3

print(a == b)

a != b

a < b

a > b

a <= b

b >= b

print(a > 0 and b > 0)

# ifAで書き直すと
if a > 0:
    if b > 0:
        print('a and b is potitive')

a > 0 or b > 0

# in と Notの使い所
y = [1, 2, 3]
x = 1

if x in y:
    print('x in y')

if 100 not in y:
    print('100 not in y')


a = 1
b = 2
# notで可読性が低くなる
if not a == b:
    print('a is not b')
# こうかけるので！
if a !=b:
    print('a is not b')


# boolen型の否定のときに使うといい
is_ok = True
if not is_ok:
    print('hello')

# 値は入っていないかの判定テクニック
# False → 0, 0.0, '', [], (), {}, set()
# 空はfalseと判定される

is_ok = set()
if is_ok:
    print('ok!')
else:
    print('no!')

# Noneを判定する場合 -> Nullオブジェクトの判定
is_empty = None
print(help(None))
# Noneかどうかを判定するときに== はあまり進められていない is を用いる
if is_empty is not None:
    print('None!')

# isは同じオブジェクトかどうかを判定する?(あまり気にしない)
print(1 == True) #True
print(1 is True) #false
print(None is None)

