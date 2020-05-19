# iteratorがないとカウントを増やしていく処理を書く必要がある
"""
num_list = [1,2,3,4,5]
count = 0
while count < len(num_list):
    print(num_list[count])
    count += 1
"""
# イテレータ(Iterator) →  反復処理を繰り返すもの
# forを使うとiteratorが使える用いる(iにリストの先頭から要素がはいる。厳密には違うかも。。)
"""
num_list = [1,2,3,4,5]
for i in num_list:
    print(i)

for s in 'abcdefg':
    print(s)

for word in ['My', 'name', 'is', 'kazuki']:
    if word == 'name':
        break
    print(word)
"""

# for else文
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        # elseを実行せずにループから抜ける
        break
    print(fruit)
else:
    print('I ate all!')