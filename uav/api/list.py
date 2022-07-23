#导包
import  requests
import app


#计划list接口
class listApi:
    def __init__(self,list_url):
        self.list_url = app.BASE_URL + "/api/v2/inspectionSchedule/list"

    def get_list(self,session,airportId,current,size,state,scheduleName,creator,startCreatetime,endCreatetime,orgPath,scheduleInspectionType):
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
        return session.post(url=self.list_url,json=list_data,headers=app.headers_data)
