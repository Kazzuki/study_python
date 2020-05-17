print('hello')
print("hello")
print('I don\'t now')
print('hello.\nHow are you?')
print(r'C:\name\name') #rは生データであることを指定する

print("################")
#\は次にデータが続くことを指定する
print("""\
line1
line2
line3\
""")
print("################")

print("kauzki\n" * 5)
s =('aaaaaaaaaaaaaaaaaaaa'
    'dddddddddddddddddddd')
print(s)

word = 'python'
print(word) 
print(word[0]) #スライス
print(word[1]) #スライス
print("################")
print(word[0:5]) #スライス
print("################")
print(word[:2])
print("################")
print(word[2:])
word = 'j' + word[1:]
print(word)
n = len(word[1:])
print(n)
print(word[:])

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('C')
print(is_start)

print("################")
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

#formatは型変換(strで型変換できるよ)されている

'a is {}'.format('a')
'a is {} {} {}'.format(1,2,3)
'a is {2} {1} {0}'.format(1,2,3)
'My name is {name} {family}'.format(name='kazuki', family='matsuda')
str(1)

#Python3.6からformatではなく、f-stringsになりました！

a = 'a'
print(f'a is {a}')
 
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
 
name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')