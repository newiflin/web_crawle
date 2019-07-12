import pymongo
from bson.objectid import ObjectId

# 1.连接MongoDb
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# 2.指定数据库
db = client.test
# db = client['test']
# 3.指定集合
collection = db.students
# Collection = db['students']
# 4.插入数据
# student = {
#     'id': '20190712',
#     'name': 'Pan',
#     'age': 22,
#     'gender': 'male'
# }
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)
# student1 = {
#     'id': '20180808',
#     'name': 'Peter',
#     'age': 20,
#     'gender': 'femail'
# }
# student2 = {
#     'id': '20190101',
#     'name': 'Lisa',
#     'age': 19,
#     'gender': 'male'
# }
# results = collection.insert_many([student1, student2])
# print(results)
# print(results.inserted_ids)

# 5.查询数据
result = collection.find_one({'name': 'Lisa'})
print(type(result))
print(result)
result = collection.find_one({'_id': ObjectId('5d2845e2a3116138434670b4')})
print(type(result))
print(result)

results = collection.find({'age': {'$gt': 18}})
print(type(results))
for result in results:
    print(result)

# 6.计数
count1 = collection.find().count()       # count已过时
print(count1)
count2 = collection.find({'age': {'$gt': 21}}).count()
print(count2)

# 7.排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 8.偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(60)    #从第61个开始
print([result['name'] for result in results])
results = collection.find().sort('name', pymongo.ASCENDING).skip(10).limit(2)
print([result['name'] for result in results])

# 9.更新
condition = {'name': 'Lisa'}
student = collection.find_one(condition)
student['name'] = 'Anto'
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age' : {'$gt': 19}}
result = collection.update_one(condition, {'$inc': {'age': 1}}) #选择年龄大于19学生的第一条年龄+1
print(result)
print(result.matched_count, result.modified_count)

result = collection.update_many(condition, {'$inc': {'age': 1}}) #选择多条
print(result)
print(result.matched_count, result.modified_count)

# 10.删除
result = collection.delete_one({'name': 'Lisa'})
print(result)
print(result.deleted_count)
result = collection.delete_one({'age': {'$gt' : 23}})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$gt': 23}})
print(result)
print(result.deleted_count)