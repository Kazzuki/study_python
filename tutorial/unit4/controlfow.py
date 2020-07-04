while True:
    x = int(input("整数を入力してください: "))
    if x <= 10:
        print("{}は10以下です".format(x))
    elif 10<x and x<=25:
        print("{}は10より大きく25以下です".format(x))
    else:
        print("{}は25より大きいです".format(x))
        break


# s = input("整数を入力してください: ")
# print(s)
# print(type(s))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#         print('Single')
# else:
#         print('More')