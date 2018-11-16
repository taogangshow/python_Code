import redis

try:
    r = redis.StrictRedis(host='localhost',port=6379)
    print(r)
except Exception as message:
    print(message)

# 方式一：根据数据类型的不同，调用相应的方法，完成读写
# 更多方法同前面学的命令
# r.set('name','hello')
# r.get('name')
# 方式二：pipline
# 缓冲多条命令，然高后一次性执行，减少服务器-客户端之间TCP数据库包，从而提效率
'''写'''
# pipe = r.pipeline()
# pipe.set('py10', 'hello')
# pipe.set('py11', 'world')
# pipe.execute()

'''读'''
temp = r.get('py10')
print(temp)
