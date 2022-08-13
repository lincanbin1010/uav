import json
import unittest
from parameterized import parameterized
import app
from api import uavtasksave
import utils
from time import strftime
#构造测试数据
def build_data():
    file = "./data/tasksave.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        json_data = json.load(f) #加载json文件
        for case_data in json_data:
            routeId = case_data.get("routeId")
            taskName = case_data.get("taskName")
            coveringArea = case_data.get("coveringArea")
            executor = case_data.get("executor")
            taskType = case_data.get("taskType")
            subId = case_data.get("subId")
            comments = case_data.get("comments")
            taskDes = case_data.get("taskDes")
            airportId = case_data.get("airportId")
            relation_obj = case_data.get("relation_obj")
            taskMode = case_data.get("taskMode")
            flyModeVal = case_data.get("flyModeVal")
            flyMode = case_data.get("flyMode")
            returnMode = case_data.get("returnMode")
            flySpeed = case_data.get("flySpeed")
            initSpeed = case_data.get("initSpeed")
            workSpeed = case_data.get("workSpeed")
            routeName = case_data.get("routeName")
            totalPoint = case_data.get("totalPoint")
            totalSecond = case_data.get("totalSecond")
            totalDist = case_data.get("totalDist")
            totalShootPoint = case_data.get("totalShootPoint")
            offsetDistance = case_data.get("offsetDistance")
            aerialDirection = case_data.get("aerialDirection")
            routeMissionType = case_data.get("routeMissionType")
            cameraMode = case_data.get("cameraMode")
            returnAlt = case_data.get("returnAlt")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((routeId,taskName,coveringArea,executor,taskType,subId,comments,taskDes,airportId,relation_obj,taskMode,flyModeVal,flyMode,
                              returnMode,flySpeed,initSpeed,workSpeed,routeName,totalPoint,totalSecond,totalDist,totalShootPoint,offsetDistance,aerialDirection,routeMissionType,cameraMode,returnAlt,status_code,code,msg))
            print(test_data)
    return test_data

#创建测试类
class Testuavtasksave(unittest.TestCase):
    def setUp(self):
        self.uavtasksave_api = uavtasksave.uavtasksaveApi()

    @parameterized.expand(build_data())
    #航线审核测试用例
    def test_uavtasksave_1(self,routeId,taskName,coveringArea,executor,taskType,subId,comments,taskDes,airportId,relation_obj,taskMode,flyModeVal,flyMode, returnMode,flySpeed,initSpeed,workSpeed,routeName,totalPoint,totalSecond,totalDist,totalShootPoint,offsetDistance,aerialDirection,routeMissionType,cameraMode,returnAlt,status_code,code,msg):
        routeId = app.complexRoute_id
        taskName = "测试{}".format(strftime("%Y%m%d%H%M%S"))
        subId = app.substationId
        airportId = app.airportID

        response = self.uavtasksave_api.get_tasksave_url(routeId,taskName,coveringArea,executor,taskType,subId,comments,taskDes,airportId,relation_obj,taskMode,flyModeVal,flyMode,returnMode,flySpeed,initSpeed,workSpeed,routeName,totalPoint,totalSecond,totalDist,totalShootPoint,offsetDistance,aerialDirection,routeMissionType,cameraMode,returnAlt)
        print(response.json())

        #调用断言方法
        utils.get_ass(self,status_code,code,msg,response)