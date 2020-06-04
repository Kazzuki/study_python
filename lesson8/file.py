#91 'w'→書き込み,'a'→追加,'r'→読み込み

"""
f = open('lesson8/test.txt', 'w')
f.write('kakakkakakkazuzuuzuzkiiikiki\n')
print('My', 'name', 'is', 'kazuki', sep='#', end='!', file=f)
f.close()
"""


#92(★)wihtステイトメント
# fileのcloseを書き忘れないように良いとされる書き方
"""
with open('lesson8/test.txt','a') as f:
    f.write('\nwhitステイトメント最高！！\n')
"""

#93 ファイルの読み込み
with open('lesson8/test.txt','r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break