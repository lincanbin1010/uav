import app
from api.searchrouteid import searchrouteidApi
import unittest
import requests
import json
from parameterized import parameterized


#构造数据
def build_data():
    file ="./data/searchrouteid.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            current = case_data.get("current")
            size = case_data.get("size")
            substationId = case_data.get("substationId")
            routeId = case_data.get("routeId")
            routeName = case_data.get("routeName")
            routeGroup = case_data.get("routeGroup")
            routeType = case_data.get("routeType")
            startDate = case_data.get("startDate")
            endDate = case_data.get("endDate")
            airportId = case_data.get("airportId")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((current,size,substationId,routeId,routeName,routeGroup,routeType,startDate,endDate,airportId, status_code, code, msg))
            print(test_data)
    return test_data


#创建测试类
class TestSearchrouteid(unittest.TestCase):

    def setUp(self):
        self.searchrouteid_api =searchrouteidApi()

    @ parameterized.expand(build_data())

#获取航线ID用例
    def test08_searchrouteid_1(self,current,size,substationId,routeId,routeName,routeGroup,routeType,startDate,endDate,airportId,status_code,code,msg):

        #查询航线ID接口
        response = self.searchrouteid_api.get_searchrouteid(current,size,substationId,routeId,routeName,routeGroup,routeType,startDate,endDate,airportId)
        print(response.json())

        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertEqual(code,response.json().get("code"))
        self.assertIn(msg,response.json().get("msg"))

