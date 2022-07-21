#导包
import unittest
import requests
from api.login import LoginApi

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

#创建测试用例

#登录成功
    def test01_login_success(self):
        #调用验证码接口
        response = self.login_api.get_verify_code(self.session)
        #断言
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers.get("Content-Type"))

        #调用登录接口
        response = self.login_api.get_url_login(self.session,"13488888888","123456","8888")
        #断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(1,response.json().get("status"))
        self.assertIn("登录成功",response.json().get("msg"))



#账号不存在
    def test01_user_isnot_exist(self):
        #调用验证码接口
        response = self.login_api.get_verify_code(self.session)
        #断言
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers.get("Content_Type"))

        #调用登录接口
        response = self.login_api.get_url_login(self.session,"134888888889","123456","8888")
        #断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(1,response.json().get("status"))
        self.assertIn("操作成功",response.json().get("msg"))
#密码错误
    def test03_password_error(self):
        #调用验证码接口
        response = self.login_api.get_verify_code(self.session)
        #断言
        self.assertEqual(200,response.status_code)
        self.assertIn("image",response.headers.get("Content_Type"))

        #调用登录接口
        response = self.login_api.get_url_login(self.session,"13488888888","1234567","8888")
        #断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(1,response.json().get("status"))
        self.assertIn("操作成功",response.json().get("msg"))




