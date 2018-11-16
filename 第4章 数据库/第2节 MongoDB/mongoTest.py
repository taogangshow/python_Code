import pymongo

#连接，创建客户端
client = pymongo.MongoClient("localhost", 27017)

#获得数据库t_py3
db=client.t_py3
#获得集合stu
t_stu = db.t_stu
#增加
# sql_insert={'name': 'hr', 'age': 16}
# s1 = t_stu.insert_one(sql_insert)
# print(s1)
#修改
# s2 = t_stu.update_one({'name': 'hr'}, {'$set': {'name': 'abc'}})
# print(s2)
#删除
# s3 = t_stu.delete_one({'name': 'abc'})
# print(s3)
#查询
cursor = t_stu.find({'age': {'$gt':20}}).sort('_id', 1).skip(1).limit(1)
for result in cursor:
    #print(result)
    print(result['name'])