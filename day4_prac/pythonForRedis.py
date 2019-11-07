# 导入redis
import redis
from redisPool import POOL

'''
pool = redis.ConnectionPool(host='localhost', port=6379, db=0, password='')
redis = redis.Redis(connection_pool=pool)
# 连接redis
# redis = redis.Redis(host='localhost', port=6379, db=0, password='')
redis.set('name', 'Bob')
print(redis.get('name'))

# 字符串操作
# set设置
redis.set('name', '张三')
# 参数：
# set(name, value, ex=None, px=None, nx=False, xx=False)
# ex:过期时间（秒）
# px:过期时间（毫秒）
# nx:如果设置为True，则只有name不存在的时候当前set才会执行
# xx:如果设置为True，则只有那么存在的时候当前set才会操作

print(redis.get('name').decode('utf8'))
# redis还可以使用url来创建连接
# redis://[:password]@host:port/db
# rediss://[:password]@host:port/db
# unix://[:password]@/path/to/socket.sock?db=db
pool1 = redis.ConnectionPool(host='localhost', port=6379, db=1)
url = 'redis://@localhost:6379/0'
pool = redis.ConnectionPool.from_url(url)
conn = redis.Redis(connection_pool=pool)
conn.set('testkey', 'testValue')
print(conn.get('testkey'))      # b'testValue'
# 判断一个键是否存在exists(keyname)
print(conn.exists('testkey'))  # 1   True
# 删除一个键delete(keyname)

# 判断键的类型type(keyname)
print(conn.type('testkey'))      # b'string'
# 获取所有符合规则的键keys(pattern)
pattern = 't*'
print(conn.keys(pattern))       # [b'testkey']
# 获取一个随机的键randomkey()
print(conn.randomkey())         # b'language'
# 重命名键rename(src, dst) src:原键名，dst：新键名
conn.rename('testkey', 'keyname')
print(conn.keys('keyname'))     # [b'keyname']
# 获取当前数据库中键的数量dbsize()
print(conn.dbsize())            # 3
# 设置键的过期时间，单位：秒 expire(keyname, time)

# 获取键的过期时间，单位：秒，-1表示永不过期 ttl(keyname)
print(conn.ttl('keyname'))      # -1 永不过期
# 将键移至其他数据库 move(keyname, db)  db为数据库编号
conn.move('keyname', 2)
print(conn.dbsize())        # 2
print(conn.keys('keyname'))  # []
# 删除当前数据库中的所有键 flushdb()
# conn.flushdb()
# print(conn.dbsize())        # 0
# 删除所有数据库中的所有键 flushall()
conn1 = redis.Redis(connection_pool=pool1)      # 1
print(conn1.dbsize())
conn.flushall()
print(conn1.dbsize())   # 0
print(conn.dbsize())    # 0
'''
conn = redis.Redis(connection_pool=POOL)
# 字符串操作
# set(name, value) 给数据库中键为name的string赋予值value
conn.set('testkey', 'testvalue')
# get(name) 返回数据库中键为name的string的value
data = conn.get('testkey')
print('testkey的value是{}'.format(data))  # testkey的value是b'testvalue'
# getset(name, value)   给数据库中键为name的string赋予值value并返回上次的value
print(conn.getset('keyname', 'newtestvalue'))
# mget(keys, *args)  返回多个键对应的value
l = []
for i in range(10):
    name = 'name' + str(i)
    key = 'key' + str(i)
    conn.set(name, key)
    l.append(name)
print(conn.mget(*l))    # [b'key0', b'key1', b'key2', b'key3', b'key4', b'key5', b'key6', b'key7', b'key8', b'key9']
# setnx(name, value)  如果不存在这个键值对，则更新value，否则不变
print(conn.get('name1'))   # b'key1'
conn.setnx('name1', 'xxxx')
print(conn.get('name1'))    # b'key1'
conn.setnx('nameX', 'xxxx')
print(conn.get('nameX'))    # b'xxxx'
# setex(name, time, value)  设置可以对应的值为string类型的value，并指定此键值对应的有效期,name:键名,time:有效期；value：值

# setrange(name, offset, value) 设置指定键的value值的子字符串
# redis.set('name', 'Hello')    redis.setrange('name', 6, 'World')
# mset(mapping) 批量赋值 mapping:字典
# msetnx(mapping)   键均不存在时才批量赋值
# incr(name, amount=1)  键为name的value增值操作（+amount），默认为1，键不存在则被创建并设value为amount
# decr(name, amount=1)  键为name的value减值操作，默认为1，键不存在则被创建并将value设置为-amount
# append(key, value)    键为name的string的值附加value（追加内容到value）
# substr(name, start, end=-1)   返回键为name的string的子串 end默认为-1
# getrange(key, start, end)     获取键的value值从start到end的子字符串
