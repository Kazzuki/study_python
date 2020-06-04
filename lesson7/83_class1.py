class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('{} run'.format(self.model))

class ToyotaCar(Car):
    def run(self):
        print('Toyota is fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                enable_auto_run=False,
                passwd = '123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd
    
    # propertyをつけることにより、_enable_auto_runが読み込み専用の属性になった
    @property
    def enable_auto_run(self):
        return self._enable_auto_run 
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
        
    def auto_run(self):
        print('auto_run')
    def run(self):
        print('Tesla is king!!!')
car = Car('kazuki')
car.run()

print('###############')
toyota_car = ToyotaCar()
toyota_car.run()

print('###############')
tesla_car = TeslaCar('Model kazuki',passwd='456')
tesla_car.run()
tesla_car.auto_run()

#83. プロパティを使った属性の設定
# AttributeErrorが発生する(読み込みはできるが、書き込みができなくなる)
tesla_car._enable_auto_run = True
print(tesla_car._enable_auto_run)

# _enable_auto_run →外部からはいじられたくな事を明示的に示す(実は外部からアクセスはできるが。。)なので、@propertyやsetterの処理を追加してくれ〜
# __enable_auto_run にするとクラス内からのみアクセスできる
