# -*- coding:utf-8 -*-
import time
from MysqlHelper import MysqlHelper
from hashlib import sha1

def verify_user_input(user_name,user_pwd):
    # 对密码加密
    s1 = sha1()
    s1.update(user_pwd.encode("utf-8"))
    enc_user_pwd = s1.hexdigest()
    # 根据用户名查询密码
    helper = MysqlHelper('localhost', 3306, 'root', 'mysql', 'python3')
    sql = "select passwd from users where name = %s"
    params = [user_name]
    count = helper.get_all(sql, params)
    # 验证
    if len(count) == 0:
        print("输入的用户名不正确...")
        # In[1]: s = (('40bd001563085fc35165329ea1ff5c5ecbdbbeef',),)
        # In[2]: s[0][0]
        # Out[2]: '40bd001563085fc35165329ea1ff5c5ecbdbbeef'
    elif count[0][0] == enc_user_pwd:
        print("登录成功...")
    else:
        print("输入的密码不正确...")


def verify_user_new_input(new_user_name,new_user_pwd):
    s1 = sha1()
    s1.update(new_user_pwd.encode("utf-8"))
    enc_new_user_pwd = s1.hexdigest()
    helper = MysqlHelper('localhost', 3306, 'root', 'mysql', 'python3')
    #1.判断用户输入的新的用户名是否已经存在
    sql = "select * from users where name = %s"
    params = [new_user_name]
    count = helper.get_one(sql, params)
    #2.当执行sql语句查询时当用户输入的新用户名无法在users表中查询到时，此时count返回的结果是None
    if count == None:
        print("正在注册中...请稍后...")
        time.sleep(1)
        return insert_new_user(new_user_name,enc_new_user_pwd)
    else:
        print("用户名已存在，请重新输入...")
        return None

def insert_new_user(new_user_name,enc_new_user_pwd):
    helper = MysqlHelper('localhost', 3306, 'root', 'mysql', 'python3')
    sql = "insert into users(name,passwd) values(%s,%s)"
    params = [new_user_name,enc_new_user_pwd]
    count = helper.insert(sql, params)
    if count==1:
        print("注册成功...")
        return count
    else:
        print("注册失败...")
        return None

def print_menu():
    print("欢迎访问xxxx网站")
    print("1.老用户登录----")
    print("2.新用户注册----")
    print("3.退出访问------")

def main():
    print_menu()
    while True:
        num = int(input("请选择功能:"))
        if num == 1:
            # 接收用户输入
            user_name = input("请输入用户名:")
            user_pwd = input("请输入密码:")
            verify_user_input(user_name,user_pwd)
        elif num == 2:
            while True:
                new_user_name = input("请输入新的用户名:")
                new_user_pwd = input("请输入新的密码:")
                result = verify_user_new_input(new_user_name,new_user_pwd)
                if result is not None:
                    break
        elif num == 3:
            print("正在退出...请稍后...")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
#接收用户输入
# user_name = input("请输入用户名:")
# user_pwd = input("请输入密码:")

#对密码加密
# s1 = sha1()
# s1.update(user_pwd.encode("utf-8"))
# new_user_pwd = s1.hexdigest()

#根据用户名查询密码
# helper = MysqlHelper('localhost', 3306, 'root', 'mysql', 'python3')
# sql = "select passwd from users where name = %s"
# params = [user_name]
# count = helper.get_all(sql,params)
# #验证
# if len(count) == 0:
#     print("输入的用户名不正确...")
#     # In[1]: s = (('40bd001563085fc35165329ea1ff5c5ecbdbbeef',),)
#     # In[2]: s[0][0]
#     # Out[2]: '40bd001563085fc35165329ea1ff5c5ecbdbbeef'
# elif count[0][0] == new_user_pwd:
#     print("登录成功...")
# else:
#     print("输入的密码不正确...")

"""以上代码还可以推展到验证注册---1.用户名是否重复之类的"""