#导包
import app
import requests

#计划list接口
class listApi:
    def __init__(self):
        self.list_url = app.BASE_URL + "/api/v2/inspectionSchedule/list"

    def get_list(self,airportId,current,size,state,scheduleName,creator,startCreatetime,endCreatetime,orgPath,scheduleInspectionType):
        list_data = {
            "airportId": airportId,
            "current": current,
            "size": size,
            "state":state,
            "scheduleName": scheduleName,
            "creator": creator,
            "startCreatetime": startCreatetime,
            "endCreatetime": endCreatetime,
            "orgPath": orgPath,
            "scheduleInspectionType": scheduleInspectionType
        }
        return requests.post(url=self.list_url,json=list_data,headers=app.headers_data)
