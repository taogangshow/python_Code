import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql', db='python3', charset='utf8')
    cursor1 = conn.cursor()
    name = input("请输入要添加的名字:")
    sql = "insert into students(name) values(%s)"
    count = cursor1.execute(sql, [name])
    print(count)
    conn.commit()
    cursor1.close()
    conn.close()
except Exception as result:
    print(result)
"""
其它语句
cursor对象的execute()方法，也可以用于执行create table等语句
建议在开发之初，就创建好数据库表结构，不要在这里执行
"""