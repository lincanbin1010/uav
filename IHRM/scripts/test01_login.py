#导包
from api.login import LoginAPI
import  unittest

#创建测试类
class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginAPI()

    def test01_case001(self):
        response = self.login_api.login({"mobile":"13800000002","password":"123456"})
        print(response.json())

        #断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    def test02_case002(self):
        response = self.login_api.login({"mobile":"138000000022","password":"123456"})
        print(response.json())

        #断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))