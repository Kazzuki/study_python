# (★)クラスの定義
# class Person(): でも class Person: でもいい！
# メソッドの第一引数にはselfをつけないと行けないみたい
class Person(object):
    # objectが生成された時点で実行される→objectが作られる時にはじめに実行されるものコンストラクタ(初期値をセットしたり)
    def __init__(self, name):
        self.name = name
    def say_something(self):
        print("hello. I'm {}!".format(self.name))
        self.run(10)
    def run(self, num):
        print('run' * num)
    # デストラクタ→objectがなくなる時に実行される→del 〇〇がない場合はコードを実行し終えてデストラクタが動く
    def __del__(self):
        print("I'll be back!!!!")


# psesonにオブジェクトが作られる
person = Person('kazuki')
print(person)
print(type(person))

person.say_something()
del person
print('###########')

# クラスの継承,オーバーライド、super()による親クラスの要請
# オーバーライド -> メソッド名を同じにして子クラスのメソッドを実行できる
class Car(object):
    def __init__(self, model=None):
        # self.modelはクラス内の変数を指し、クラス内で保有している
        self.model = model
    def run(self):
        print('{} run'.format(self.model))
# 継承する際は→子クラス(親クラス)と宣言する
class ToyotaCar(Car):
    # passは何もしない意味
    # pass
    def run(self):
        print('Toyota is fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # 以下は親クラスの__init__を使えばいいので,super()で呼び出す
        # self.model = model
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
    def auto_run(self):
        print('auto_run')
    def run(self):
        print('Tesla is king!!!')
car = Car('kazuki')
car.run()

print('###############')
toyota_car = ToyotaCar()
toyota_car.run()

print('###############')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

