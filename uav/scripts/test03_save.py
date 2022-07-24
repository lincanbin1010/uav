#导包
import json
from parameterized import parameterized
import  unittest
import app
from api.save import saveApi
#构造测试数据
def build_data():
    file ="./data/save.json"
    test_data =[]
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f)  # 加载JSON文件数据
        for case_data in json_data:
            scheduleName = case_data.get("scheduleName")
            taskList = case_data.get("taskList")
            airportId = case_data.get("airportId")
            validDate = case_data.get("validDate")
            expireDate = case_data.get("expireDate")
            scheduleType = case_data.get("scheduleType")
            scheduleInformation = case_data.get("scheduleInformation")
            totalRetry = case_data.get("totalRetry")
            scheduleInspectionType = case_data.get("scheduleInspectionType")
            inspectionType = case_data.get("inspectionType")
            startTime = case_data.get("startTime")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((scheduleName,taskList,airportId,validDate,expireDate,scheduleType,scheduleInformation,totalRetry,startTime,inspectionType,scheduleInspectionType, status_code, code, msg))
            print(test_data)
    return test_data

#创建测试类
class Testsave(unittest.TestCase):
    def setUp(self):
        self.save_api =saveApi()

    @parameterized.expand(build_data())

    #测试用例
    def test03_save1(self,scheduleName,taskList,airportId,validDate,expireDate,scheduleType,scheduleInformation,totalRetry,startTime,inspectionType,scheduleInspectionType,status_code,code,msg):
        #调用save接口
        self.taskList =[{"index": 1, "task":app.RECORDS0, "length": "", "startTime": "19:47:56"}, {"index": 2,"task":app.RECORDS1, "length": "", "startTime": "19:51:17"}]
        taskList=self.taskList
        response = self.save_api.get_save_url(scheduleName,taskList,airportId,validDate,expireDate,scheduleType,scheduleInformation,totalRetry,startTime,inspectionType,scheduleInspectionType)
        print(response.json())
        print(taskList)
        #断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))
