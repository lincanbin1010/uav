#导包
#航线上传接口
import requests
import app


class routeuploadApi:
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
        self.file = {"file": ("upload_test_line.json", open(r"E:\luyao\FILE\JMETER\upload_test_line.json", "rb"), "application/json", {})}
        return requests.post(url=self.routeuploadUrl,data=routeupload_data,headers=app.headers_FormData)