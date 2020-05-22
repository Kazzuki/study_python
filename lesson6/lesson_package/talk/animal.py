import lesson_package.tools.utils as utils

def sing():
    return 'jlfkalsdlfjajksdf'

def cry():
    return utils.say_twice('jjksadlfjasdl')

# 77.mainでimportされてもif以下は実行されない！
if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)