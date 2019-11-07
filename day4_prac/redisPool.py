import redis

# 建立连接缓冲池
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379)
