#导包
import  pymysql

#连接数据库
conn = pymysql.connect (
    host= "localhost",
    port= 3306,
    user= "root",
    password= "123456789",
    database= "books",
    autocommit= True
)

#获取游标
cursor = conn.cursor()

#执行SQL

sql = "INSERT  INTO t_book VALUES(5,'BA','2022-07-07','1','2','0')"
cursor.execute(sql)
print("影响结果总共行数：", cursor.rowcount)
print('-'*50)

raise Exception('出错了')

sql = "INSERT  INTO t_book VALUES(6,'CA','2022-07-07','1','2','0')"
cursor.execute(sql)
print("影响结果总共行数：", cursor.rowcount)
#关闭游标
cursor.close()

#关闭连接
conn.close()
