import pymysql

try:
    #1.创建对象：调用connect()方法,用于连接数据库
    conn=pymysql.connect(host='localhost', port=3306, db='python3', user='root', passwd='mysql', charset='utf8')
    #2.返回Cursor对象，用于执行sql语句并获得结果
    cursor1=conn.cursor()
    #3.创建要执行sql语句
    sql = "insert into students(id,name) values(14,'张良')"
    #4.execute(operation[, parameters])执行语句，返回受影响的行数
    count=cursor1.execute(sql)
    #打印影响的行数
    print(count)
    #5.commit()事务，所以需要提交才会生效
    conn.commit()
    #6.关闭Cursor对象连接
    cursor1.close()
    #7.关闭数据库连接对象连接
    conn.close()
except Exception as result:
    print(result)

