import csv

with open('lesson8/test1.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    #CSVファイルの書き込みオブジェクトを生成
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #csvファイルにheaderが書き込まれる(Name,Count)
    writer.writeheader()
    #csvファイルにデータを追加する
    writer.writerow({'Name': 'kazuki', 'Count': 23})
    writer.writerow({'Name': 'yui', 'Count': 22})
    writer.writerow({'Name': 'taisei', 'Count': 22})
    writer.writerow({'Name': 'ooki', 'Count': 54})

with open('lesson8/test1.csv', 'r') as csv_file:
    #CSVファイルの読み込みオブジェクトを生成
    reader = csv.DictReader(csv_file)
    #一行ずつ読んでやる
    for row in reader:
        print(row['Name'],row['Count'])
    