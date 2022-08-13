import json
import unittest
from parameterized import parameterized
import app
from api import uavtasksave
import utils
#构造测试数据
def build_data():
    file = "./data/predictFlyData.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f) #加载json文件
        for case_data in json_data:
            id = case_data.get("id")
            speed = case_data.get("speed")
            taskMode = case_data.get("taskMode")
            airportId = case_data.get("airportId")
            initSpeed = case_data.get("initSpeed")
            returnMode = case_data.get("returnMode")
            auxHeight = case_data.get("auxHeight")
            returnAlt = case_data.get("returnAlt")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((id,speed,taskMode,airportId,initSpeed,returnMode,auxHeight,returnAlt,status_code,code,msg))
            print(test_data)
    return test_data

#创建测试类
class TestpredictFlyData(unittest.TestCase):
    def setUp(self):
        self.predictFlyData_api = uavtasksave.uavtasksaveApi()

    @parameterized.expand(build_data())
    #生成航线数据测试用例
    def test_predictFlyData_1(self,id,speed,taskMode,airportId,initSpeed,returnMode,auxHeight,returnAlt,status_code,code,msg):
        id =app.complexRoute_id
        airportId =app.airportID
        response = self.predictFlyData_api.get_predictFlyData_url(id,speed,taskMode,airportId,initSpeed,returnMode,auxHeight,returnAlt)
        print(response.json())

        #调用断言方法
        utils.get_ass(self,status_code,code,msg,response)