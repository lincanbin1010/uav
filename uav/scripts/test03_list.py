from api.list import listApi
import unittest
import requests
import json
from parameterized import parameterized


#构造数据
def build_data():
    file ="./data/list.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            airportId = case_data.get("airportId")
            current = case_data.get("current")
            size = case_data.get("size")
            state = case_data.get("state")
            scheduleName = case_data.get("scheduleName")
            creator = case_data.get("creator")
            startCreatetime = case_data.get("startCreatetime")
            endCreatetime = case_data.get("endCreatetime")
            orgPath = case_data.get("orgPath")
            scheduleInspectionType = case_data.get("scheduleInspectionType")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((airportId,current,size,state,scheduleName,creator,startCreatetime,endCreatetime,orgPath,scheduleInspectionType, status_code, code, msg))
            print(test_data)
    return test_data


#创建测试类
class Testlist(unittest.TestCase):

    def setUp(self):
        self.list_api =listApi()
        # self.session = requests.session()

    # def tearDown(self):
    #     if self.session:
    #         self.session.close()

    @ parameterized.expand(build_data())

#计划列表查询
    def test_list_ok(self,airportId,current,size,state,scheduleName,creator,startCreatetime,endCreatetime,orgPath,scheduleInspectionType,status_code,code,msg):

        #调用登录接口
        response = self.list_api.get_list(airportId,current,size,state,scheduleName,creator,startCreatetime,endCreatetime,orgPath,scheduleInspectionType)
        print(response.json())
        print("##########------------###########")
        #断言
        self.assertEqual(status_code,response.status_code)
        self.assertEqual(code,response.json().get("code"))
        self.assertIn(msg,response.json().get("msg"))
