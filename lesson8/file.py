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
"""
with open('lesson8/test.txt','r') as f:
    # while True:
    #     chunk = 2
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break
    #seekを使う
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    f.seek(3)
    print(f.read(1))
"""

#95 ファイルの書き込み＋読み込み
"""
#'w+'→書き込みと読み込み。'r+'→読み込みと書き込み(ファイルが無ければエラーになる)
with open('lesson8/test1.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

"""
