import requests
import app

class deleteApi:
    def __init__(self):
        self.deleteUrl = app.BASE_URL+"/api/v2/inspectionSchedule/delete"

    def get_delete_url (self,idList,airportId):
        delete_data ={
            "idList":idList,
            "airportId":airportId
        }
        return requests.post(self.deleteUrl,json=delete_data,headers=app.headers_data)
