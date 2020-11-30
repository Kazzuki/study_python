import configparser

''' configfileの書き出し
# 実行ファイルの場所にconfig.iniを書き出す('w')
config = configparser.ConfigParser()
config['DEAULT'] = {
    'debug': True 
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}

config['db_server'] = {
    'host': '127.0.0.1',
    'port': 80
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)
'''


config = configparser.ConfigParser()
# read
config.read('config.ini')
# section
print(config['DEAULT'])
# sectionとキー
print(config['web_server']['host'])
print(config['db_server']['port'])
