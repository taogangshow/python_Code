import redis


class RedisHelper(object):
    def __init__(self, host, port):
        self.__redis = redis.StrictRedis(host, port)

    def get(self, key):
        #判断是否存在键，存在返回true,不存在返回false
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return None

    def set(self, key, value):
        self.__redis.set(key, value)
