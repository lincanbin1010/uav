#封装被测试系统接口
import requests

import app


class PostmanApi:
#初始化
    def __init__(self):
        self.url2= app.BASE_URL+"/api/v2/inspectionRoute/json"

#登录
    def get_postman(self):
        payload = {'routeName': 'upload_test_line',
                   'airPortId': '',
                   'description': '',
                   'routeType': '2',
                   'routeGroup': '0',
                   'comments': '',
                   'substationId': 'lee0000',
                   'fileType': '10'}
        files = [
            ('file',
             ('upload_test_line.json', open(r"E:\luyao\FILE\JMETER\upload_test_line.json", 'rb'), 'application/json'))
        ]
        headers=app.headers_FormData
        return requests.request("POST", url=self.url2, headers=headers, data=payload, files=files)