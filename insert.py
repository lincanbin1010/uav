#导包
import pymysql

#创建连接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456789",
                       database="books",
                       autocommit="true"
)
#创建游标
cursor = conn.cursor()
#执行sql

sql="INSERT INTO t_book (id,title,pub_date) VALUES(4,'西游记','1986-01-01');"
cursor.execute(sql)

#获取受影像的结果总行数
print("获取数据库总行数为",cursor.rowcount)


#关闭游标
cursor.close()
#关闭连接
conn.close()