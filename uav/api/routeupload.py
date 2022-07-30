#导包
#航线上传接口
import requests
import app


class RouteuploadApi:
    def __int__(self):
        self.routeuploadUrl =app.BASE_URL + "/api/v2/inspectionRoute/json"


    def get_routeupload_url(self,routeName,airPortId,description,routeType,routeGroup,comments,substationId,fileType):
        routeupload_data={
            "routeName":routeName,
            "airPortId": airPortId,
            "description": description,
            "routeType": routeType,
            "routeGroup": routeGroup,
            "comments": comments,
            "substationId": substationId,
            "fileType": fileType
        }
        files = [
            ('file',('upload_test_line.json', open(r"E:\luyao\FILE\JMETER\upload_test_line.json", 'rb'), 'application/json'))
        ]
        return requests.request("POST", url=self.routeuploadUrl, headers=app.headers_FormData, data=routeupload_data, files=files)
        # files = {"file": ("upload_test_line.json", open(r"E:\luyao\FILE\JMETER\upload_test_line.json", "r"), "application/json", {})}
        # return requests.post(url=self.routeuploadUrl,data=routeupload_data,headers=app.headers_FormData,files=files)