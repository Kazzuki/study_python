#Pythonにはコメントを上に書くという暗黙のルールが存在する

# Apple price
some_value = 100

print('xxxxxxxxx')
"""
test
test
test
"""
print('xxxxxxxxx')

# 80文字以上になる場合は次の行に行くこと
# コードが長くなるときの対応

#パレンティス版
s = ('aaaaaaaaaaaaaaaaa'
    + 'bbbbbbbbbbbbbbbb')
print(s)

x = (1 + 1 + 1 + 1 + 1 
    + 1 + 1 + 1)
print(x)

#\版
s = 'aaaaaaaaaaaaaaaaa'\
    'bbbbbbbbbbbbbbbb' 
print(s)

# 数字の場合うまくなった？
# x = 1 + 1 + 1 + 1 + 1 \ 
#     + 1 + 1 + 1
print(x)