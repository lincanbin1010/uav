#导包
import  pymysql

#连接数据库
conn = pymysql.connect (
    host= "localhost",
    port= 3306,
    user= "root",
    password= "123456789",
    database= "books"
)

#获取游标
cursor = conn.cursor()

#执行SQL

sql = "select * from t_book"
cursor.execute(sql)

print("结果总共行数：", cursor.rowcount)

print(cursor.fetchall())

#重置游标位置
cursor.rownumber=0
print(cursor.fetchone())

#关闭游标
cursor.close()

#关闭连接
conn.close()
