import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql', db='python3', charset='utf8')
    cursor1 = conn.cursor()
    sql = "update students set birthday = '1992-10-10' where id = 14"
    count = cursor1.execute(sql)
    print(count)
    conn.commit()
    cursor1.close()
    conn.close()
except Exception as result:
    print(result)