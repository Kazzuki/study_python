# Docstrings
# 関数の説明は関数内に書く

# def example_func(param1, param2):
#     """Example function with types documented in the docstring.(関数の概要を書く)

#     Args:
#         params1 (int): hogehoge
#         params2 (str): hogehoge
#     Returns:
#         bool: hogehogeohge
#     """
#     print(param1)
#     print(param2)
    # return True

# .__doc__で関数の説明を表示できる→help
# print(example_func.__doc__)

# 関数内関数→その関数内でしか使わない関数を定義する
# def outer(a, b):

#     def plus(c, d):
#         return c + d
    
#     r1 = plus(a,b)
#     r2 = plus(b,a)
#     return(r1 + r2)

# r = outer(1,2)
# print(r)

# クロージャー(?)→56講義を確認
# 用途がよくわからんけど。レベル高い感じ
# はじめに設定した引数を用いて用途によって使い分けたい時に使う

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    print(circle_area)
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))

# デコレーター(?)→57講義を確認
# 何かで包み込むイメージ
"""
コード書いてません(Udemyで確認してみて！)
"""

