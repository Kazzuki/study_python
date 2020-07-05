try:
    a = int(input("割られる数"))
    b = int(input("割る数"))
    result = a/b
except ZeroDivisionError as ex:
    print(ex)
    print("０で割ったらあかんやろ！！")
except ValueError as ex:
    print(ex)
    print("文字列は困ります")
else:
    print(result)
finally:
    print("finallyブロックは絶対実行されるで！")