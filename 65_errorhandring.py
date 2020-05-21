# 例外処理→エラーが発生してもプログラムを停めずに最後まで処理させる
# tyrでIndexErrorをチャッチして次のプログラムにすすめる！

l = [1,2,3]
i = 5
try:
    # IndexErrorが発生する
    l[i]
except:
    print("Don't worry!") 


# Pythonのエラー階層参考（https://docs.python.org/3.6/library/exceptions.html#exception-hierarchy）

l = [1,2,3]
i = 5

try:
    l[0]
except IndexError as ex:
    print("Don't worry!: {}".format(ex)) 
except NameError as ex:
    print(ex) 
# ほぼ全てのエラーに該当するExceptionで、エラーをキャッチすることはよくない！
except Exception as ex:
    print("other: {}".format(ex))
# エラーにかかることがなく終わるとき
else:
    print('Done')
# 必ず最後に実行される
finally:
    print('clean up')


print('############################')

# 独自例外の作成→例外は自分で起こすことができる!
# 自分たち独自のエラーに対して処理をかけるので開発の効率が上がる
#  raise NameError('kakakkakakka')

#Exceptionを継承したUppercaseErrorクラスを定義している
class UppercaseError(Exception):
    pass
        #この中に付け加えたい処理を書いていく

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next!{}'.format(exc))