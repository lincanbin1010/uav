import requests

import app
#任务查询接口
class searchrouteidApi:
    def __init__(self):
        self.searchrouteidApiUrl =app.BASE_URL+"/api/v2/inspectionRoute/search"

    def get_searchrouteid(self,current,size,substationId,routeId,routeName,routeGroup,routeType,startDate,endDate,airportId):
        search_data={
            "current":current,
            "size": size,
            "substationId": substationId,
            "routeId": routeId,
            "routeName": routeName,
            "routeGroup": routeGroup,
            "routeType": routeType,
            "endDate": endDate,
            "startDate": startDate,
            "airportId": airportId
        }
        return requests.post(url=self.searchrouteidApiUrl,json=search_data,headers=app.headers_data)

