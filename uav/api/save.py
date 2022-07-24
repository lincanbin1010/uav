#导包
import requests
import app

#创建save接口
class saveApi:
    def __init__(self):
        self.saveUrl=app.BASE_URL+"/api/v2/inspectionSchedule/save"

    def get_save_url(self,scheduleName,taskList,airportId,validDate,expireDate,scheduleType,scheduleInformation,totalRetry,startTime,inspectionType,scheduleInspectionType):
        save_data={
            "scheduleName": scheduleName,
            "taskList":taskList,
            "airportId": airportId,
            "validDate": validDate,
            "expireDate": expireDate,
            "scheduleType": scheduleType,
            "scheduleInformation": scheduleInformation,
            "totalRetry": totalRetry,
            "startTime":startTime,
            "inspectionType":inspectionType,
            "scheduleInspectionType":scheduleInspectionType

        }
        return requests.post(url=self.saveUrl,json=save_data,headers=app.headers_data)