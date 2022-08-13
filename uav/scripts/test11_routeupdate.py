import json
import unittest
from parameterized import parameterized
import app
from api import routeupdate
import utils
#构造测试数据
def build_data():
    file = "./data/routeupdate.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f) #加载json文件
        for case_data in json_data:
            routeId = case_data.get("routeId")
            state = case_data.get("state")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((routeId,state,status_code,code,msg))
            print(test_data)
    return test_data

#创建测试类
class Testrouteupdate(unittest.TestCase):
    def setUp(self):
        self.routeupdate_api = routeupdate.routeupdateApi()

    @parameterized.expand(build_data())
    #航线审核测试用例
    def test_routeupdate_1(self,routeId,state,status_code,code,msg):
        routeId = app.route_id_0
        response = self.routeupdate_api.get_routeupdate_url(routeId, state)
        print(response.json())

        #调用断言方法
        utils.get_ass(self,status_code,code,msg,response)