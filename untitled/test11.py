from dbutil import DBUtil

sql ="select * from t_book"
result = DBUtil.exe_sql(sql)
print(result)