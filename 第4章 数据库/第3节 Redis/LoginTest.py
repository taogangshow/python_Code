from MysqlHelper import MysqlHelper
from RedisHelper import RedisHelper
from hashlib import sha1
# 用户登录
# 业务过程如下：
# 输入用户名、密码
# 密码加密
# 判断redis中是否记录了用户名，如果有则成功
# 如果redis中没有用户名，则到mysql中查询
# 从mysql中查询成功后，将用户名记录到redis中

#1.获取用户的输入
user_name = input("请输入用户名:")
user_pwd = input("请输入密码:")
#2.对用户的密码进行加密
s1 = sha1()
s1.update(user_pwd.encode("utf-8"))
enc_user_pwd = s1.hexdigest()
#3.查询redis中是否存在此用户
r = RedisHelper('localhost',6379)
m = MysqlHelper('localhost', 3306, 'root', 'mysql', 'python3')
#print(r.get('user_name')) for test
#当在redis查询结果为空时，在mysql中查询密码
#print(r.get(user_name)) for test
if r.get(user_name)==None:
    sql = 'select passwd from users where name =%s'
    params = [user_name]
    passwd = m.get_one(sql, params)
    # print(passwd) for test
    #判断用户是否存在
    if passwd == None:
        print("用户名不存在....")
    else:
        #将mysql查询的结果存到redis中，因为redis的键相同会被替换，所以这里set name 直接为用户名
        r.set(user_name, passwd[0])
        #判断密码是否正确
        if passwd[0]==enc_user_pwd:
            print("验证成功...")
        else:
            print("密码错误1...")
else:
    if r.get(user_name).decode("utf-8") == enc_user_pwd:
        print("记录redis数据库成功...")
    else:
        print("密码错误2...")

