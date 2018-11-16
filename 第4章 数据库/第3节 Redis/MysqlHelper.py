import pymysql


class MysqlHelper(object):
    """封装
    (观察前面的文件发现，除了sql语句及参数不同，其它语句都是一样的)"""
    def __init__(self,host, port, user, passwd, db, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()
    #.查询一条数据
    def get_one(self,sql,params=()):
        try:
            self.connect()
            self.cur.execute(sql,params)
            result = self.cur.fetchone()
            self.close()
            return result
        except Exception as e:
            print(e)

    #查询全部数据
    def get_all(self,sql,params=()):
        try:
            self.connect()
            self.cur.execute(sql,params)
            list = self.cur.fetchall()
            self.close()
            return list
        except Exception as e:
            print(e)

    def insert(self,sql,params=()):
        return self.__edit(sql,params)

    def update(self,sql,params=()):
        return self.__edit(sql, params)

    def delete(self,sql,params=()):
        return self.__edit(sql, params)
    #这个方法用来增删改,因为查询不需要commit()
    def __edit(self, sql, params):
        try:
            self.connect()
            count = self.cur.execute(sql,params)
            self.conn.commit()
            self.close()
            return count
        except Exception as e:
            print(e)
