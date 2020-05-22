
# lesson_package.talk.animalのテスト用に書いていたスクリプトが実行されてしまう！
import lesson_package.talk.animal
# configにprintなどが書いてあればimportした時点で実行されてしまう
import config


# __main__と表示される→このスクリプトを実行しているmainのプログラムですという意味
print('lesson:',__name__) 


# (★)重要！！本来のpythonではこの様に書くのが当たり前！
# これまでの問題(importされたら知らない内に実行されちゃう問題)を踏まえて、本来は下の用に書く！
def main():
    print('hello')

if __name__ == '__main__':
    main()