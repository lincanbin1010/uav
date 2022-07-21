#导包
import pymysql
#创建连接
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456789",
                       database="books",
                       autocommit= True

)
#创建游标
cursor = conn.cursor()
#执行sql
sql = "update t_book set title='西游记' where title='东游记';"
cursor.execute(sql)
print(cursor.rowcount)
#关闭游标
cursor.close()

#关闭连接
conn.close()