# 名前空間とスコープ
animal = 'cat'

def f():
    animal = 'dog'
    print('after:', animal)

f() #local val -> animal
print('global:',animal) #global bal -> animal

animal1 = 'kazuki'
def f1():
    # 関数名でグローバル変数を書き換える
    global animal1 
    animal1 = 'yui'
    print('after:', animal1)

f1() 
print('global:',animal1) 


# ローカル変数、グローバル変数を表示する
# __val__ はPythonが事前に用意しているもの勝手に置き換えないように注意！

animal2 = 'kintama'
def f2():
    """Test func doc"""
    hoge = 'hogehoge'
    print('local',locals())
    print(f2.__name__)
    print(f2.__doc__)

f2()
# print('global val:',globals()) 
print(__name__)