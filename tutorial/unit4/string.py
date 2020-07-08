"""
チャレンジ問題p102
"""
str = "カミュ"
for i in str:
    print(i)


str1 = input("入力1:")
str2 = input("入力2:")
print("私は{}に{}をした".format(str1, str2))

print("kazuki".capitalize())
print("ka zu ki".split("k"))

test_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
new_list = " ".join(test_list)
print(new_list)

test1_str = "A screaming comes across the sky"
new_test1_str = test1_str.replace("s","$")
print(new_test1_str)

test2_str = "Hemingway"
new_test2_index = test2_str.index("m")
print(new_test2_index)

three_str = "three" + "three" + "three"
print(three_str)
three_str1 = "three" * 3
print(three_str1)

test3_str = "4月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(test3_str.split("、"))