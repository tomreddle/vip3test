# 导入MySQLdb
import MySQLdb

# # 建立数据库连接
# db = MySQLdb.connect(host='127.0.0.1',
#                      port=3306,
#                      user='root',
#                      passwd='root',
#                      database='test')
# # 建立游标
# cursor = db.cursor()
#
# # 待执行sql,创建表employee
# sql = '''create table employee(id char(20) not null,
#     name char(20),
#     age int,
#     sex char(1))'''
# # 执行sql
# try:
#     cursor.execute(sql)
#     print("执行成功\n" + sql)
# except BaseException as msg:
#     print("sql语句执行失败")
#     print(msg)
# # 关闭数据库连接
# db.close()
#
# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# # 使用sql插入数据
# # 建立数据库连接
# db = MySQLdb.connect(host='127.0.0.1',
#                      port=3306,
#                      user='root',
#                      passwd='root',
#                      database='test')
# # 建立游标
# cursor = db.cursor()
# # 执行插入sql
# insert_sql = '''insert into employee values("20191111", "Hulk", "42", "M")'''
# # 执行插入sql
# try:
#     cursor.execute(insert_sql)
#     db.commit()
#     print("sql执行成功")
# except BaseException as msg:
#     print("sql执行失败")
#     print(msg)
#     db.rollback()
# # 关闭数据库连接
# db.close()
# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# # 修改数据库数据
# db = MySQLdb.connect(host='127.0.0.1',
#                      port=3306,
#                      user='root',
#                      passwd='root',
#                      database='test')
# # 建立游标
# cursor = db.cursor()
# # updatesql
# update_sql = '''update employee set age = "30" where id = "20191111"'''
# # 执行update语句
# try:
#     cursor.execute(update_sql)
#     db.commit()
#     print("sql执行成功")
# except BaseException as msg:
#     print("sql执行失败")
#     print(msg)
#     db.rollback()
# # 关闭数据库连接
# db.close()
# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# # 查询数据库数据
# db = MySQLdb.connect(host='127.0.0.1',
#                      port=3306,
#                      user='root',
#                      passwd='root',
#                      database='test')
# cursor = db.cursor()
# select_sql = '''select * from employee where age >= "35" and sex = "M"'''
# # 执行sql
# try:
#     cursor.execute(select_sql)
#     # 获取查询结果
#     data = cursor.fetchall()
#     print(data)
# except BaseException as msg:
#     print(msg)
# # 关闭数据库连接
# db.close()

# 删除数据库数据
db = MySQLdb.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='root',
                     database='test')
cursor = db.cursor()
delete_sql = '''delete from employee where age <= "35" and sex = "M"'''
# 执行sql
try:
    cursor.execute(delete_sql)
    db.commit()
    print("数据删除成功")
except BaseException as msg:
    print(msg)
    db.rollback()
# 关闭数据库连接
db.close()
