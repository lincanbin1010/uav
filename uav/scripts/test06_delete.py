import json

from api.delete import deleteApi

import unittest
import requests

from parameterized import  parameterized
import  app

#构造测试数据
def build_data():
    file ="./data/delete.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            idList = case_data.get("idList")
            airportId = case_data.get("airportId")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((idList, airportId, status_code, code, msg))
            print(test_data)
    return test_data


#创建测试类
class Testdelete(unittest.TestCase):
    def setUp(self):
        self.delete_api =deleteApi()

    @parameterized.expand(build_data())
    #删除计划
    def test06_delete1(self,idList,airportId,status_code,code,msg):

        self.idList=[app.SCHID]
        idList =self.idList
        print(idList)
        self.airportId =app.airportID
        airportId=self.airportId
        print(airportId)

        response =self.delete_api.get_delete_url(idList,airportId)
        print(response.json())

        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))