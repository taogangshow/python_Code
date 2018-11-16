import pymysql
"""查询学生信息"""
try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql', db='python3', charset='utf8')
    cur = conn.cursor()
    sql = "select * from students"
    num = cur.execute(sql)
    print(num)
    count = cur.fetchall()
    for i in count:
        print(i)
    conn.close()
    cur.close()
except Exception as result:
    print(result)