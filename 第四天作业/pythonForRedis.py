# 导入redis
import redis

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


