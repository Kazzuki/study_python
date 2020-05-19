#while
"""
count = 0
while count < 5:
    print(count)
    # 以下を忘れると無限ループになる
    count += 1 
"""
#while, break, continue
# break → ループを抜ける
# continue → 次のループに移る
"""
count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        # continueはwhileの先頭に戻る？
        continue

    print(count)
    count += 1
"""

# while else
"""
count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
# breakで抜けない限り最後の実行される
else:
    print('done')
"""

# input関数
input_num =[]
while True:
    # string型で入力される
    word = input('Enter:') 
    num = int(word)
    if num == 100:
        break
    input_num.append(num)
    print(input_num)
    print('next')
