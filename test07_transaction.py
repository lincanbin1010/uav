#导包
import pymysql

conn = None
cursor =None
try :
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="123456789",
                           database="books"
                           )
    # 创建游标
    cursor = conn.cursor()
    sql = "INSERT INTO t_book (id,title,pub_date) VALUES(4,'西游记','1986-01-01');"
    cursor.execute(sql)
    print(cursor.rowcount)

    #raise Exception("出错啦！")

    sql = "INSERT INTO t_book (id,title,pub_date) VALUES(5,'老游记','1986-10-10');"
    cursor.execute(sql)
    print(cursor.rowcount)

    raise Exception("出错啦！")
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)

finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭连接
    if conn:
        conn.close()