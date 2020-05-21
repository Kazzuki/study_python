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
    # IndexErrorが発生する
    l[i]
except:
    print("Don't worry!") 

# 独自例外の作成