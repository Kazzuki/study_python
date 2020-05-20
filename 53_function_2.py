def menu(entree='beef', drink='wine'):
    print(entree,drink)

menu(entree='beef',drink='coffee')

# キーワード引数の辞書化
def menu1(**kwargs):
    # {'entree': 'beef', 'drink': 'coffee'}の辞書型で表示される
    print(kwargs) 
    # 辞書型を展開して表示
    for k, v in kwargs.items():
        print(k,v)

menu1(entree='beef',drink='coffee')

# 以下の様にも渡せる
d = {
    'a': '1',
    'c': '2',
    'd': '3'
}
menu1(**d)

#(★)位置引数、タプル、辞書をまとめる
def menu2(food, *args, **kwargs):
    # banana
    print(food)
    # ('apple', 'orange')
    print(args)
    # {'entree': 'beef', 'drink': 'coffee'}
    print(kwargs)

menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')

