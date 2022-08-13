import json
import unittest
from parameterized import parameterized
import app
from api import uavtasksave
import utils
#构造测试数据
def build_data():
    file = "./data/complexRoute.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f) #加载json文件
        for case_data in json_data:
            dbRouteId = case_data.get("dbRouteId")
            speed = case_data.get("speed")
            airportId = case_data.get("airportId")
            aerialDirection = case_data.get("aerialDirection")
            returnMode = case_data.get("returnMode")
            auxHeight = case_data.get("auxHeight")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((dbRouteId,speed,airportId,aerialDirection,returnMode,auxHeight,status_code,code,msg))
            print(test_data)
    return test_data

#创建测试类
class TestcomplexRoute(unittest.TestCase):
    def setUp(self):
        self.complexRoute_api = uavtasksave.uavtasksaveApi()

    @parameterized.expand(build_data())
    #航线审核测试用例
    def test_complexRoute_1(self,dbRouteId,speed,airportId,aerialDirection,returnMode,auxHeight,status_code,code,msg):
        dbRouteId = app.route_id_0
        airportId = app.airportID
        response = self.complexRoute_api.get_complexRoute_url(dbRouteId,speed,airportId,aerialDirection,returnMode,auxHeight)
        print(response.json())

        #提取data航线ID数据
        app.complexRoute_id = response.json().get("data")
        print(app.complexRoute_id)

        #调用断言方法
        utils.get_ass(self,status_code,code,msg,response)