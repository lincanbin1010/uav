import requests

import app


class TakeoffSaveApi:
    def __init__(self):
        self.takeoff_url = app.BASE_URL + "/api/v2/vehicleTakeoffTitle/save"

    def get_takeoffurl(self, lat, lon, name, takeOffOffset, taskIdList, substationId, alt):
        data = {
            "lat": lat,
            "lon": lon,
            "name": name,
            "takeOffOffset": takeOffOffset,
            "taskIdList": taskIdList,
            "substationId": substationId,
            "alt": alt
        }
        return requests.post(url=self.takeoff_url,json=data,headers=app.headers_data)