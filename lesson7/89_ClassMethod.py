# オブジェクトが生成されるタイミングを理解する
# クラスメソッド、クラス変数はインスタンス(オブジェクト)が生成されなくてもアクセスできる

class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100
    
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind


a = Person()
print(a.x)
print(a.kind)

b = Person #bはオブジェクトとして生成れていない
# よって以下はxを持っていないのでAttributeErrorが起こる
# print(b.x)
#kindはクラス変数なので参照可能
print(b.kind)
# what_is_your_kindはクラスメソッドなので参照できる
print(b.what_is_your_kind())


