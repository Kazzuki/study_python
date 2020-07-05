# 入力した数値の二乗を返す関数を作る

def hoge():
    def double(x=1, y=1, z=1):
        return x * y * z

    input_number1 = int(input("代入してええよ:"))
    input_number2 = int(input("代入してええよ:"))
    input_number3 = int(input("代入してええよ:"))

    result = double(input_number1, input_number2, input_number3)
    print(result)

hoge()
hoge()