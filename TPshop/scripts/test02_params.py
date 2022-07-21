#导包
import json
import unittest
import requests
from api.login import LoginApi
from parameterized import  parameterized

#构造数据
def build_data():
    file = "../data/login.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        json_data =json.load(f) #加载JSON文件数据
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            verify_code = case_data.get("verify_code")
            content_type = case_data.get("content_type")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((username,password,verify_code,content_type,status_code,status,msg))
            print(test_data)
    return test_data






#创建测试类
class TestLogin(unittest.TestCase):

#前置处理
    def setUp(self):
        self.login_api = LoginApi()  #实例化接口
        self.session = requests.Session()  #创建session 对象


#后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())
#创建测试用例

#登录成功
    def test01_login_success(self,username,password,verify_code,content_type,status_code,status,msg ):
        #调用验证码接口
        response = self.login_api.get_verify_code(self.session)
        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertIn(content_type,response.headers.get("Content-Type"))

        #调用登录接口
        response = self.login_api.get_url_login(self.session,username,password,verify_code)
        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertEqual(status,response.json().get("status"))
        self.assertIn(msg,response.json().get("msg"))



