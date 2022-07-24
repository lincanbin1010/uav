import requests
import app

class updateApi:
    def __init__(self):
        self.updateUrl = app.BASE_URL+"/api/v2/inspectionSchedule/update"

    def get_update_url (self,state,scheduleId):
        update_data ={
            "state":state,
            "scheduleId":scheduleId
        }
        return requests.post(self.updateUrl,json=update_data,headers=app.headers_data)
