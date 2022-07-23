#导包
import  requests
import app

#计划list接口
class listApi:
    def __init__(self,list_url):
        self.list_url ="/api/v2/inspectionSchedule/list"

    def get_list(self,airportId,current,size,state,scheduleName,creator,startCreatetime,endCreatetime,orgPath,scheduleInspectionType):
        self.list_data = {
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
        return requests.post(url=self.list_url,json=self.list_data,headers=app.headers_data)
