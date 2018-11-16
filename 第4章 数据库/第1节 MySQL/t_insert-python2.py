#coding:utf-8
# import MySQLdb
# 
# try:
#     conn=MySQLdb.connect(host='localhost', port=3306, db='python3', user='root', passwd='mysql', charset='utf8')
#     cursor1=conn.cursor()
#     sql = "insert into students(id,name) values(14,'张良')"
#     count=cursor1.execute(sql)
#     print(count)
#     conn.commit()
#     cursor1.close()
#     conn.close()
# except Exception as result:
#     print(result)