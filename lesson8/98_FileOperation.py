#98(★) ファイル操作(ライブラリー名を覚えておけば大概の事はできる)  

import os
#空のファイルを簡単に作れる
import pathlib

import glob
# ディレクトリをまたいでコピー可
import shutil
#ファイルが階層に存在するか
# print(os.path.exists('test.py'))

#fileかどうか？
# print(os.path.isfile('test.py'))

#dirかどうか？
#print(os.path.isdir('lesson8/design'))

# file名の変更
# os.rename('test.py', 'kazuki.py')

# symlink
# os.symlink('kintama.txt','symlink.txt')

# dirの作成・削除
# os.mkdir('test_dir')
#  os.rmdirはdirectoryが空でないと事項出来ない
# os.rmdir('test_dir')

# 空fileの作成
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

#ディレクトリは再帰的に作成できそう
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')

#directoryに何があるかをlistで表示する
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()

# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')

print(glob.glob('test_dir/test_dir2/*'))

#ディレクトリを丸々削除できるので、使用には注意！！
shutil.rmtree('test_dir')
#PWD的なやつ
print(os.getcwd())

