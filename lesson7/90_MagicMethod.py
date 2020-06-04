# 特殊メソッドは__fun__となっているモノ(アンダースコアが前後にあるもの)
# __str__がよく使われるよ！

class Word(object):

    def __init__(self, text):
        self.text = text

    #文字列が呼ばれると表示される
    def __str__(self):
        return 'Word!!!!!!!!!'

    def __len__(self):
        return len(self.text)
    
    # def __eq__(self, word):
    #     return self.text.lower() == word.text.lower()
    
w = Word('test')
print(w)

# lenを返す
print(len(w)) #__len__が呼ばれる
# 本来ならばこうなる
print(len(w.text))

w2 = Word('test')
print(w == w2) #__eq__が呼ばれる
print(id(w))
print(id(w2))
print(w == w2) #__eq__がなければ、違うobject同士なのでFalseが返る