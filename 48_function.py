# 上からスクリプトを読み込むので、関数定義を行ってから関数を呼び出すこと

def say_something():
    print('Hi')

# say_sometnigは<class 'function'>である
print(type(say_something)) 
#この様にも実行できる
f = say_something
f()

# 戻り値(複数の戻り値を返す)
def test_something():
    s = 'hi'
    m = 100
    return s,m

result = test_something()
print(result)
# 戻り地が複数ある場合は<class 'tuple'>タプル型で返って来る
print(type(result))

# 引数
def what_is_this(color):
    if color == 'red':
        return 'tomoto'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know."

result = what_is_this('green')
print(result)
