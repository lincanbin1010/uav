from api.search import searchApi
from parameterized import  parameterized
import requests
import unittest

import json

#构造数据
def build_data():
    file ="./data/search.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            airportId = case_data.get("airportId")
            current = case_data.get("current")
            executor = case_data.get("executor")
            size = case_data.get("size")
            subId = case_data.get("subId")
            taskMode = case_data.get("taskMode")
            msg = case_data.get("msg")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            test_data.append((airportId,current,executor,size,subId,taskMode, status_code, code, msg))
            print(test_data)
    return test_data


#创建测试类

class Testsearch:
    def setUp(self):
        self.search_api =searchApi()


    def tearDown(self):
        pass

    # 构造数据
    def build_data():
        file = "./data/login.json"
        test_data = []
        with open(file, encoding="utf-8") as f:
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

    @parameterized.expand(build_data())

    #任务查询
    def test01_search(self,airportId,current,executor,size,subId,taskMode,status_code,code,msg):
        response =self.search_api.get_search(self,airportId,current,executor,size,subId,taskMode)
        print(response.json())
        #断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))

