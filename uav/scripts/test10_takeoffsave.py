import json
from time import strftime

import app
from api import takeoffsave
import unittest
from parameterized import  parameterized
#构造数据
def build_data():
    file = "./data/takeoffsave.json"
    test_data=[]
    with open(file,encoding="UTF-8") as f:
        json_data = json.load(f) #加载json文件数据
        for case_data in json_data:
            lat = case_data.get("lat")
            lon = case_data.get("lon")
            name = case_data.get("name")
            takeOffOffset = case_data.get("takeOffOffset")
            taskIdList = case_data.get("taskIdList")
            substationId = case_data.get("substationId")
            alt = case_data.get("alt")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((lat, lon, name, takeOffOffset, taskIdList, substationId, alt, status_code, code, msg))
    return test_data



#创建测试类
class Testtakeoffsave(unittest.TestCase):
    def setUp(self):
        self.takeoffsave_api = takeoffsave.TakeoffSaveApi()

    @parameterized.expand(build_data())
    def test10_takeoffsave1(self, lat, lon, name, takeOffOffset, taskIdList,  substationId, alt, status_code, code, msg):
        self.taskIdList =["%s"%(app.task_id_0),"%s"%(app.task_id_1)]
        taskIdList = self.taskIdList
        name = "移动巡检{}".format(strftime("%Y%m%d-%H%M%S"))
        response = self.takeoffsave_api.get_takeoffurl(lat, lon, name, takeOffOffset, taskIdList, substationId, alt)
        print(response.json())
        print(taskIdList)
        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertEqual(code,response.json().get("code"))
        self.assertIn(msg,response.json().get("msg"))