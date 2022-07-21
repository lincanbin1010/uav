import requests
import unittest
from api.login import LoginApi
from tools.dbutil import DBUtil
from parameterized import  parameterized

#构造数据
def build_data():
    #获取数据库数据
    sql = "select * from login"
    db_data = DBUtil.exe_sql(sql)
    test_data =[]

    for case_data in db_data:
         username = case_data[1]
         password = case_data[2]
         vcode = case_data[3]
         status_code = case_data[5]
         code = case_data[4]
         msg = case_data[6]
         test_data.append((username, password, vcode, status_code, code, msg))
         print(test_data)
    return test_data


#创建测试类
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login_api =LoginApi()
        self.session = requests.session()

    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())

#登录
    def test01_login(self,username,password,vcode,status_code,code,msg):

        #调用登录接口
        response = self.login_api.get_url_login(self.session,username,password,vcode)
        print(response.json())
        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertEqual(code,response.json().get("code"))
        self.assertIn(msg,response.json().get("msg"))




