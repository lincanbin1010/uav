import  requests
import app
#创建航线审核类
from app import BASE_URL


class routeupdateApi:
    def __init__(self):
        self.routeupdate_url = BASE_URL + "/api/v2/inspectionRoute/update"

    #航线审核
    def get_routeupdate_url(self,routeId,state):
        data = {
            "routeId": routeId,
            "state": state
        }
        return requests.post(url=self.routeupdate_url, json=data,headers=app.headers_data)

