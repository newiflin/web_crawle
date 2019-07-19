from redis import StrictRedis, ConnectionPool

# 1.连接redis
redis = StrictRedis(host='120.76.58.229', port=6379, db=0, password=123456)
redis.set('name', 'Tony')
print(redis.get('name'))

pool = ConnectionPool(host='120.76.58.229', port=6379, db=0, password=123456)
redis = StrictRedis(connection_pool=pool)
redis.set('age', '22')
print(redis.get('age'))

url = 'redis://:123456@120.76.58.229:6379/0'    #[连接方式]://[:password]@host:port/db
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('gender', 'male')
print(redis.get('gender'))

# 2.键的操作
print(redis.exists('name'))
print(redis.delete('gender'))
print(redis.type('name'))
print(redis.keys('a*'))
print(redis.randomkey())    #获取一个随机的键
print(redis.rename('name', 'nickname'))
print(redis.dbsize())       #获取当前数据键数
print(redis.expire('nickname', 60))
print(redis.ttl('nickname'))
print(redis.move('nickname', 1))
print(redis.flushdb())      #清空当前数据库中的键
print(redis.flushall())     #清空所有数据库中的键

# 3.字符串操作
print()
print(redis.set('emotion', 'smile'))
redis.set('name', 'Leo')
redis.set('age', '19')
print(redis.get('emotion'))
print(redis.getset('emotion', 'humour'))
print(redis.mget(['emotion', 'name', 'age']))
print(redis.setnx('newname', 'James'))      # 不存在键才更新
print(redis.setex('country', 1, 'china'))
redis.setrange('name', 3, '2019')
print(redis.get('name'))
print(redis.mset({'name1': 'Modric', 'name2': 'Van Dik'}))
print(redis.msetnx({'name3': 'Salah', 'name4': 'Mane'}))    #键均不存在才批量更新
print(redis.incr('age', 1))
print(redis.decr('age', 1))
print(redis.append('name', 'ooo'))
print(redis.substr('name', 1, 4))
print(redis.getrange('name', 0, 3))

# 4.列表操作
print(redis.rpush('list', 1, 2, 3, 4, 5))
print(redis.lpush('list', 0))
print(redis.llen('list'))
print(redis.lrange('list', 1, 3))
print(redis.ltrim('list', 1, 3))
print(redis.lindex('list', 1))
print(redis.lset('list', 1, 666))
print(redis.lrem('list', 1, 1))
print(redis.lpop('list'))
print(redis.rpop('list'))
#print(redis.blpop('list'))
#print(redis.brpop('list'))
#print(redis.brpoplpush('list'))     #删除列表尾元素，添加到列表头部

# 5.集合操作
print(redis.sadd('tags', 'Book', 'Tea', 'Coffee'))
print(redis.srem('tags', 'Book', 'Coffee'))
print(redis.spop('tags'))
print(redis.smove('tags', 'tags2', 'Tea'))
print(redis.scard('tags'))
print(redis.sismember('tags', 'Tea'))
redis.sadd('tags', 'Book', 'Tea', 'Coffee')
redis.sadd('tags2', 'Tea')
print(redis.sinter(['tags', 'tags2']))          #集合的交集
print(redis.sinterstore('inttag', ['tags', 'tags2']))
print(redis.sunion(['tags', 'tags2']))
print(redis.sunionstore('uiontag', ['tags', 'tags2']))
print(redis.sdiff(['tags', 'tags2']))
print(redis.sdiffstore('difftag', ['tags', 'tags2']))
print(redis.smembers('tags'))
print(redis.srandmember('tags'))

# 6.有序集合
print(redis.zadd('grade', {'Mike': 100, 'Bob': 88, 'Lee': 78, 'Ming': 99}))    #python3之后传字典
print(redis.zrem('grade', 'Bob'))
print(redis.zincrby('grade', 2.2, 'Mike'))              #...新版本倒一下参数就好了
print(redis.zrank('grade', 'Lee'))          #获取正数排名
print(redis.zrevrank('grade', 'Lee'))       #获取倒数排名
print(redis.zrevrange('grade', 1, 2))
print(redis.zrevrangebyscore('grade', 99, 80))
print(redis.zcount('grade', 70, 100))   #分数在70~100的元素个数
print(redis.zcard('grade'))             #统计集合grade元素个数
print(redis.zremrangebyrank('grade', 1, 3))
redis.zadd('grade', {'Mike': 100, 'Bob': 88, 'Lee': 78, 'Ming': 99})
print(redis.zrevrangebyscore('grade', 78, 100))

# 7.散列
print()
print(redis.hset('price', 'cake', 5))
print(redis.hsetnx('price', 'book', 50))
print(redis.hget('price', 'cake'))
print(redis.hmget('price', ['cake', 'book']))
print(redis.hmset('price', {'keyboard': 22, 'mouse': 10}))
print(redis.hincrby('price', 'cake', 1))
print(redis.exists('price', 'book'))
print(redis.hdel('price', 'keyboard'))
print(redis.hlen('price'))
print(redis.hkeys('price'))     #获取所有映射的键名
print(redis.hvals('price'))     #获取所有映射的键值
print(redis.hgetall('price'))   #获取所有的映射





