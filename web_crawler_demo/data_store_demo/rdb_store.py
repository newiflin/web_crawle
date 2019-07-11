import pymysql

#1.关系型数据库
connect = pymysql.connect(host='120.76.58.229', user='root', password='root', port=3306)
cursor = connect.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('Database version: ', data)
# cursor.execute('create database spiders default character set utf8')  #创建一个名为spiders的数据库
db = pymysql.connect(host='120.76.58.229', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
sql = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))'
cursor.execute(sql)

#插入操作
id = '20190712'
name = 'Luka'
age = '19'
sql = 'insert into students (id, name, age) values (%s, %s, %s)'
try:
    cursor.execute(sql, (id, name, age))
    db.commit()
except:
    db.rollback()

data = {
    'id': '20191010',
    'name': 'Meng',
    'age': '19'
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'insert into {table} ({keys}) values ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('sucessful!')
        db.commit()
except:
    print('failed!')
    db.rollback()

#更新
sql = 'update students set name = %s, age = %s'
try:
    cursor.execute(sql, ('Lucy', 22))
    db.commit
except:
    db.rollback()

#如果数据未存在则插入，已存在则更新
data = {
    'id': 20190713,
    'name': 'DeRong',
    'age': 21
}
table = 'students'
keys = ' ,'.join(data.keys())
values = ' ,'.join(['%s'] * len(data))
sql = 'insert into {table} ({keys}) values ({values}) on duplicate key update'.\
    format(table=table, keys=keys, values=values)
update = ' ,'.join([" {key} = %s".format(key=key) for key in data.keys()])
sql += update
try:
    cursor.execute(sql, tuple(data.values()) * 2)
    print('sucessful!')
    db.commit()
except:
    print('failed!')
    db.rollback()

#删除数据
table = 'students'
condition = 'age < 20'
sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#查询数据
sql = 'select * from students where age >= 20'
try:
    cursor.execute(sql)
    one = cursor.fetchone()         #取一条指针指向数据（指针初始位置在第一行）
    print('One: ', one)
    results = cursor.fetchall()     #取游标指向所在位置及以后的所有行记录
    print('Type: ', type(results))  #二重元组
    print('Results: ', results)
    for row in results:
        print(row)
except:
    print('Error!')

sql = 'select * from students where age >= 20'
try:
    cursor.execute(sql)
    print('Count: ', cursor.rowcount)
    row = cursor.fetchone()
    while row:                      #通过fetchone遍历
        print('Row: ', row)
        row = cursor.fetchone()
except:
    print('Error!')

cursor.close()
