import json

# json文本字符串转json对象 load
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)  #将json文本字符串转换为json对象
print(data)
print(type(data))       #列表类型
print(data[0]['name'])
print(data[0].get('name'))
print(data[0].get('old'))       #获取不存在的属性
print(data[0].get('old', 25))

with open('data1.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

# json对象转json字符串文本 dump
data = {
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}
with open('data2.json', 'w') as file:
    file.write(json.dumps(data, indent=2))  #indent缩进

data = {
    "name": "黎明",
    "gender": "男",
    "birthday": "2010-11-29"
}
with open('data3.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))  #取消中文转unicode
