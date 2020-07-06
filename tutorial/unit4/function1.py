"""
p69のチャレンジ問題
・数学と同じで数式を書きながら理解する過程がプログラミンで全く身についていない。
・はじめは、コードを書くことになれないかもしれないが、頭の中にある考えを表現していかないといつまで立ってもこのまま。
・文章を書く、考えを書き出す習慣があるんだから、絶対コードを書くこともできる！俺はやれる。
"""

def calcurate():
    """入力した値を二乗して返す
    Returns print(a * 2).
    
    """
    a = int(input("1つ目"))
    return print(a * 2)


def show_str(str):
    return print(str)


def five_params(a, b, c, d="hoge", e="fuga"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

def fuc1(num):
    print(num / 2)
    return num / 2

def fuc2(num):
    print(num * 4)
    return num * 4

def error_float():
    str = "hogehoge"
    try:
        type_conversion = float(str)
    except ValueError as ex:
        print("文字列をfloatって舐めんなよ！")
        print(ex)
    else:
        return type_conversion

calcurate()
show_str("hoge")
five_params("mama", "papa", "ane", "unnti")
result = fuc1(10)
fuc2(result)
error_float()
print(calcurate.__doc__)