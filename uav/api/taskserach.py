#导包

#创建测试接口类
import app
import requests

class TaskSearchApi:
    def __init__(self):
        self.tasksearchurl = app.BASE_URL+"/api/v2/inspectionTask/search"

    def get_tasksearch(self, session, current, size, executor, subId, taskName, keyName, startDate, endDate, taskMode, airportId):
        data = {
            "current": current,
            "size": size,
            "executor": executor,
            "subId": subId,
            "taskName": taskName,
            "keyName": keyName,
            "startDate": startDate,
            "endDate": endDate,
            "taskMode": taskMode,
            "airportId": airportId
        }
        return session.post(url=self.tasksearchurl, json=data, headers=app.headers_data)

