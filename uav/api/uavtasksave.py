import  requests
import app
#创建生成任务类
from app import BASE_URL

class uavtasksaveApi:
    def __init__(self):
        #生成航线地址
        self.complexRoute_url = BASE_URL + "/api/v2/inspectionTask/uav/complexRoute2"
        #生成航线数据地址
        self.predictFlyData_url = BASE_URL + "/api/v2/inspectionTask/uav/predictFlyData"
        #生成任务地址
        self.tasksave_url = BASE_URL + "/api/v2/inspectionTask/uav/save"

    #生成航线
    def get_complexRoute_url(self,dbRouteId,speed,airportId,aerialDirection,returnMode,auxHeight):
        data = {
            "dbRouteId": dbRouteId,
            "speed": speed,
            "airportId": airportId,
            "aerialDirection": aerialDirection,
            "returnMode": returnMode,
            "auxHeight": auxHeight
        }
        return requests.post(url=self.complexRoute_url, json=data,headers=app.headers_data)

    #生成航线数据
    def get_predictFlyData_url(self,id,speed,taskMode,airportId,initSpeed,returnMode,auxHeight,returnAlt):
        data = {
            "id": id,
            "speed": speed,
            "taskMode": taskMode,
            "airportId": airportId,
            "initSpeed": initSpeed,
            "returnMode": returnMode,
            "auxHeight": auxHeight,
            "returnAlt": returnAlt
        }
        return requests.post(url=self.predictFlyData_url, json=data,headers=app.headers_data)

    #生成任务
    def get_tasksave_url(self,routeId,taskName,coveringArea,executor,taskType,subId,comments,taskDes,airportId,relation_obj,taskMode,flyModeVal,flyMode,
                         returnMode,flySpeed,initSpeed,workSpeed,routeName,totalPoint,totalSecond,totalDist,totalShootPoint,offsetDistance,aerialDirection,routeMissionType,cameraMode,returnAlt):
        data = {"routeId":routeId,
        "taskName":taskName,
        "coveringArea":coveringArea,
        "executor":executor,
        "taskType":taskType,
        "subId":subId,
        "comments":comments,
        "taskDes":taskDes,
        "airportId":airportId,
        "relation_obj":relation_obj,
        "taskMode":taskMode,
        "flyModeVal":flyModeVal,
        "flyMode":flyMode,
        "returnMode":returnMode,
        "flySpeed":flySpeed,
        "initSpeed":initSpeed,
        "workSpeed":workSpeed,
        "routeName":routeName,
        "totalPoint":totalPoint,
        "totalSecond":totalSecond,
        "totalDist":totalDist,
        "totalShootPoint":totalShootPoint,
        "offsetDistance":offsetDistance,
        "aerialDirection":aerialDirection,
        "routeMissionType":routeMissionType,
        "cameraMode":cameraMode,
        "returnAlt":returnAlt
        }
        return requests.post(url=self.tasksave_url, json=data,headers=app.headers_data)
