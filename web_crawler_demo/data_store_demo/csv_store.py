import pandas as pd
import csv

#csv文件 保存含分隔符的文本
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ') #delimiter指定分隔符
    writer.writerow(['id', 'name', 'old'])
    writer.writerow(['101', 'Bob', '23'])
    writer.writerow(['102', 'Tim', '22'])
    writer.writerow(['103', 'Lisa', '30'])

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'old'])
    writer.writerows([['101', 'Bob', '23'], ['102', 'Tim', '22'], ['103', 'Lisa', '30']])

with open('data.csv', 'w') as csvfile:  #字典的方式写入
    fieldnames = ['id', 'name', 'old']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '101', 'name': 'Bob', 'old': '23'})
    writer.writerow({'id': '102', 'name': 'Tim', 'old': '22'})
    writer.writerow({'id': '103', 'name': 'Lisa', 'old': '30'})

with open('data.csv', 'a', encoding='utf-8') as csvfile:  #字典的方式写入
    fieldnames = ['id', 'name', 'old']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '201', 'name': 'newiflin', 'old': '23'})
    writer.writerow({'id': '202', 'name': '思绪', 'old': '25'})
    writer.writerow({'id': '203', 'name': '紫薯', 'old': '19'})

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

df = pd.read_csv('data.csv')
print(df)