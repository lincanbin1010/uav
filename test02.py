#导包
import pymysql

#创建连接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456789",
                       database="books",

)
#创建游标
cursor = conn.cursor()
#执行sql

sql="select * from t_book"
cursor.execute(sql)

#获取查询结果总行数
print("获取数据库总行数为",cursor.rowcount)
#获取第一行数据
print(cursor.fetchone())
#游标指向0
cursor.rownumber = 0
#获取全部数据
print(cursor.fetchall())

#关闭游标
cursor.close()
#关闭连接
conn.close()