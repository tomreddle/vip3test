import redis

# redis服务参数
host = '127.0.0.1'
port = 6379
decode_responses = True     # 为True时，写入的value位str类型，不加此参数时写入的则为字节类型
# 建立redis连接池全局变量
POOL = redis.ConnectionPool(host=host, port=port, decode_responses=True)

# 建立连接
conn = redis.Redis(connection_pool=POOL)
# 也可以直接建立连接
# conn = redis.Redis(host=host, port=port, decode_responses=True)
# conn.set('Mr.', 'How')
# '''
# key_name = conn.randomkey()
# a = conn.get(key_name)    # 测试
# b = conn.get('Mr.')
# print(a, b)
# '''
# # Hash类型
# # python中有hash()函数可将对象转为哈希值
# # hset(self, name, key, value)  name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
# # hget(self, name, key)     name对应的hash中根据key获取value
# conn.hset('hash1', 'k1', 'v1')
# conn.hset('hash1', 'k2', 'v2')
# hash_a = conn.hget('hash1', 'k1')
# print(hash_a)
#
# # hgetall(self, name)   获取对应hash name的所有键值对
# hash_all = conn.hgetall('hash1')
# print(hash_all)     # {'k1': 'v1', 'k2': 'v2'}
#
# # hmset(self, name, maping) 在name对应的hash中批量设置键值对，maping：字典
# # hmget(self, name, keys, *args) name对应的hash中批量获取键所对应的值
# dic = {'k3': 'v3', 'k4': 'v4'}
# conn.hmset('hash1', dic)
# print(conn.hmget('hash1', 'k2', 'k3'))    # ['v2', 'v3']
#
# # hlen(self, name)  获取name对应的hash中键值对的个数
# print(conn.hlen('hash1'))   # 4
#
# # hkeys(self, name) 获取name对应hash中的所有键
# print(conn.hkeys('hash1'))  # ['k1', 'k2', 'k3', 'k4']
#
# # hvals(self, name) 获取那么对应hash中所有的value
# print(conn.hvals('hash1'))  # ['v1', 'v2', 'v3', 'v4']
#
# # hexists(self, name, key)  判断name对应hash是否存在指定键
# print(conn.hexists('hash1', 'k3'))  # True
# print(conn.hexists('hash1', 'k10'))     # False
#
# # hdel(self, name, *keys)   删除指定name对应hash中的key-value
# # conn.hdel('hash1', 'k3', 'k4')
# print(conn.hdel('hash1', 'k3'))     # 成功返回1，失败返回0
# print(conn.hdel('hash1', 'k3'))     # 0
# print(conn.hkeys('hash1'))  # ['k1', 'k2', 'k4']
#
# # hincrby(self, name, key, amount=1)
# # 与hash中key对应的value相加，不存在则创建key=amount（amount是整数）
# print(conn.hincrby('hash1', 'k5', amount=1))    # 1
# print(conn.hget('hash1', 'k5'))     # ['k1', 'k2', 'k4']
#
# # list类型，类似于hash，一个name对应一个list
# # lpush(self, name, *values)    元素从list左边添加，可以添加多个
# # lpushx(self, name, values)   当name对应的list存在是才会从左边添加元素
# # lindex(self, name, index)     根据索引获取name对应list中的value
# conn.lpush('list1', '元素1', '元素2')
# conn.lpushx('list12', '元素3')
# print(conn.lindex('list1', 0))
# # print(conn.index('list12', 0))      # AttributeError: 'Redis' object has no attribute 'index'
#
# # rpush(self, name, *values)    从右侧添加，可以添加多个
# # rpushx(self, name, *values)   当name对应的list存在是才会从右边添加元素
# conn.rpush('list1', '元素3')
# print(conn.lindex('list1', 0))
#
# # llen(self, name)  获取name对应list的长度
# # lrange(self, name, start, end)    切片取值
# print(conn.llen('list1'))   # 24
# print(conn.lrange('list1', 1, -1))
#
# # linsert(self, name, where, refvalue, value) 在那么对应的list的某一个值前或后插入新值
# where : BEFORE  和  AFTER
# refvalue: 列表中的值
# value： 待插入的值
# print(conn.lindex('list1', 10))
# conn.linsert('list1', 'BEFORE', '元素2', '元素x')
# print(conn.lrange('list1', 0, -1))
# print(conn.lindex('list1', 1))

# lrem(self, name, value, num)  删除name对应list中指定的值
conn.lrem('list1', '元素x', 1)
# num: =0,删除列表中所有的指定值
#      =2，从前往后，删除两个
#      =-2，从后往前，删除两个
