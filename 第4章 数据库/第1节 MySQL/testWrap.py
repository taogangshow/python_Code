# -*- coding:utf-8 -*-
import time
from MysqlHelper import MysqlHelper

def print_menu():
    print("***---mysql数据库--***")
    print("---V1.0 from taogang--")
    print("功能选项:")
    print("1.查询一条学生表数据---")
    print("2.查询全部的学生表数据-")
    print("3.修改学生表数据-------")
    print("4.增加学生表数据-------")
    print("5.删除学生表数据-------")
    print("6.退出程序-------------")

def main():
    print_menu()
    while True:
        helper = MysqlHelper('localhost', 3306, 'root', 'mysql', 'python3')
        num = int(input("请输入操作序号:"))
        if num == 1:
            sql_select_one = "select * from students "
            one = helper.get_one(sql_select_one)
            print(one)
        elif num == 2:
            sql_select_all = "select * from students "
            all = helper.get_all(sql_select_all)
            for res in all:
                print(res)
        elif num == 3:
            update_name = input("请输入修改后的名字:")
            update_id = input("请输入要修改的id:")
            sql_update = "update students set name = %s where id = %s"
            params = [update_name, update_id]
            count = helper.update(sql_update,params)
            if count==1:
                print("修改成功")
            else:
                print(count)
        elif num == 4:
            insert_id = input("请输入要添加的id:")
            insert_name = input("请输入要添加的名字:")
            insert_birthday = input("请输入%s的生日"%insert_name)
            sql_update = "insert into students(id,name,birthday) values(%s,%s,%s)"
            params = [insert_id, insert_name,insert_birthday]
            count = helper.update(sql_update, params)
            if count==1:
                print("添加成功")
            else:
                print(count)
        elif num == 5:
            delete_id = input("请输入要删除学生的id:")
            sql_update = "delete from students where id = %s"
            params = [delete_id]
            count = helper.update(sql_update, params)
            if count==1:
                print("删除成功")
            else:
                print(count)
        elif num==6:
            break
        else:
            print("输入无效，请重新输入")
            time.sleep(1)
if __name__ == "__main__":
    main()


