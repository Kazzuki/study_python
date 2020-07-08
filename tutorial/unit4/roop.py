# 1
test_list = ["kazuki", "hage", "kakkoii"]
for str in test_list:
    print(str)
# 2
for i in range(25, 51):
    print(i)
# 3
for i, str in enumerate(test_list):
    print(i,str)
# 4
answer_list = [1,3,5,7]
while True:
    x = input("なにか入力してみろ")
    try:
        if int(x) in answer_list:
            print("正解")
            break
        else:
            print("不正解")
    except ValueError:
            if x != 'q':    
                print("数字を入力するか、qで終了します")
                continue
            else:
                break

# 5
num_list1 = [9, 1, 33, 83]
num_list2 = [8, 19, 148, 4]
new_list = list()
for x in num_list1:
    for y in num_list2:
        new_list.append(x * y)
print(new_list)