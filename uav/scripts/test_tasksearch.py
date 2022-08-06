
from api.taskserach import TaskSearchApi
from parameterized import parameterized
import requests
import unittest

import json

#构造数据
def build_data():
    file ="./data/tasksearch.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            current = case_data.get("current")
            size = case_data.get("size")
            executor = case_data.get("executor")
            subId = case_data.get("subId")
            taskName = case_data.get("taskName")
            keyName = case_data.get("keyName")
            startDate = case_data.get("startDate")
            endDate = case_data.get("endDate")
            taskMode = case_data.get("taskMode")
            airportId = case_data.get("airportId")
            msg = case_data.get("msg")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            test_data.append((current, size, executor, subId, taskName, keyName, startDate, endDate, taskMode, airportId, status_code, code, msg))
            print(test_data)
    return test_data


#创建测试类
class TestTaskSearch(unittest.TestCase):
    def setUp(self):
        self.tasksearch_api = TaskSearchApi()
        self.session = requests.session()

    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())
    #起飞点任务查询
    def test09_tasksearch(self,current, size, executor, subId, taskName, keyName, startDate, endDate, taskMode, airportId,status_code,code,msg):
        response =self.tasksearch_api.get_tasksearch (self.session, current, size, executor, subId, taskName, keyName, startDate, endDate, taskMode, airportId)
        print(response.json())
        #断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))

    #获取巡检任务record，用于save接口调用
        # app.RECORDS1= response.json().get("data").get("records")[1]
        # app.RECORDS0 = response.json().get("data").get("records")[0]
        #
        # print(app.RECORDS0 )
        #
        # print(app.RECORDS1 )

