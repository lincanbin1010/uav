import unittest

from api.postmans import PostmanApi

#创建测试类
class Testpostman(unittest.TestCase):

    def setUp(self):
        self.postman_api =PostmanApi()

#调接口
    def test999(self):
        res = self.postman_api.get_postman()
        print(res.json())