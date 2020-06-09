# pythonでコマンドを走らせる

#os より subprocessを使う 
# import os
import subprocess

# os.system('ls')
# subprocess.run(['ls','-al'])

#shllインジェクションが発生るので非推奨
subprocess.run('ls -al | grep test', shell=True)


#shllインジェクションへの対応
# →上級者向けに解説していたが、省略