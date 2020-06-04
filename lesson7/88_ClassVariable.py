# クラス変数はすべての生成されたオブジェクトが参照できるので、initに共通して持つものをクラス変数にしてあげるといい
# listはクラス変数にしない

class Person(object):
    kind = 'human'

    def __init__(self, name):
        self.name = name
    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):

    def __init__(self):
        self.words = []
    def add_word(self, word):
        self.words.append(word)
        print(self.words)

c = T()
c.add_word('kazuki')
c.add_word('kazuki2')
d = T()
d.add_word('yui')
d.add_word('yui2')

