import requests
import unittest

import app
from api.login import LoginApi
import json
from parameterized import parameterized


#构造数据
def build_data():
    file ="./data/login.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            vcode = case_data.get("vcode")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
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

        #获取token
        app.Access_Token =response.json().get("data").get("token")
        print(app.Access_Token)

        app.headers_data["Access-Token"]=app.Access_Token
        print(app.headers_data["Access-Token"])




