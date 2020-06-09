import datetime

"""
日時の表記
"""
now = datetime.datetime.now()
print(now)
# 国際基準の表記
print(now.isoformat())
# オリジナルの表記
print(now.strftime('%d/%m/%y-%H%M%S%f'))

"""
日の表記
"""
today = datetime.date.today()
print(today)
# 国際基準の表記
print(today.isoformat())
# オリジナルの表記
print(today.strftime('%d/%m/%y'))

"""
時の表記
"""
t = datetime.time(hour=2, minute=33, second=44, microsecond=100)
print(t)
# 国際基準の表記
print(t.isoformat())
# オリジナルの表記
print(t.strftime('%H_%M_%S_%f'))

"""
過去・未来の日時の表記
"""
print(now)
# d = datetime.timedelta(weeks=1)
# d = datetime.timedelta(days=365)
# d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=20)
# d = datetime.timedelta(seconds=1)
# d = datetime.timedelta(microseconds=100)

#過去
print(now - d)
#未来
print(now + d)

"""
タイムスリープ
"""
import time
print("5秒後に下ねたいいます")
time.sleep(3)
print("ゴールデンボール")

"""
エポックタイム(UNIX時間)
協定世界時 での1970年1月1日午前0時0分0秒から形式的な経過秒数として表され
"""
print(time.time())

"""
(★)ファイルのバックアップに使える
"""
import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name,"{}.{}".format(
        file_name, now.strftime('%y_%m_%d_%H_%M_%S')
    ))

with open(file_name, 'w') as f:
    f.write('test')
