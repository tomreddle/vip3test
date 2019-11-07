import redis
from redisPool import POOL

conn = redis.Redis(connection_pool=POOL)
# 测试连接
conn.set('language', 'Python')
redis_result = conn.get('language')
print(redis_result)
