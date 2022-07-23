import  requests
import app
#任务查询接口
class searchApi():
    def __init__(self):
        self.searchurl =app.BASE_URL+"/api/v2/inspectionTask/search"

    def get_search(self,airportId,current,executor,size,subId,taskMode):
        search_data={
            "airportId":airportId,
            "current": current,
            "executor": executor,
            "size": size,
            "subId": subId,
            "taskMode": taskMode
        }
        return requests.post(url=self.searchurl,json=search_data,headers=app.headers_data)

