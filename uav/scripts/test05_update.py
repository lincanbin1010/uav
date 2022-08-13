import json

from api.update import updateApi

import unittest
import requests

from parameterized import  parameterized
import  app

#构造测试数据
def build_data():
    file ="./data/update.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            state = case_data.get("state")
            scheduleId = case_data.get("scheduleId")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((state, scheduleId, status_code, code, msg))
            print(test_data)
    return test_data


#创建测试类
class Testupdate(unittest.TestCase):
    def setUp(self):
        self.update_api =updateApi()

    @parameterized.expand(build_data())
    #计划表审核
    def test05_update1(self,state,scheduleId,status_code,code,msg):
        self.scheduleId=app.SCHID
        scheduleId =self.scheduleId
        print(scheduleId)
        response =self.update_api.get_update_url(state,scheduleId)
        print(response.json())

        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))