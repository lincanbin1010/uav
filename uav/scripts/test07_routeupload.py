#导包
import unittest

import parameterized

from api.routeupload import RouteuploadApi
import json


#构造数据
# def build_data():
#     file ="./data/routeupload.json"
#     test_data =[]
#     with open(file,encoding="utf-8") as f:
#         json_data = json.load(f)  # 加载JSON文件数据
#         for case_data in json_data:
#             routeName = case_data.get("routeName")
#             airPortId = case_data.get("airPortId")
#             description = case_data.get("description")
#             routeType = case_data.get("routeType")
#             routeGroup = case_data.get("routeGroup")
#             comments = case_data.get("comments")
#             substationId = case_data.get("substationId")
#             fileType = case_data.get("fileType")
#             status_code = case_data.get("status_code")
#             code = case_data.get("code")
#             msg = case_data.get("msg")
#             test_data.append((routeName , airPortId , description, routeType, routeGroup, comments, substationId, fileType, status_code, code, msg))
#             print(test_data)
#     return test_data

#创建测试类
class Testrouteload(unittest.TestCase):
    def setUp(self):
        self.RouteUpload_api = RouteuploadApi()

    # @parameterized.parameterized.expand(build_data())

    #调用文件上传接口
    def test07_routeupload_1(self):
        # self.files = {"file": ("upload_test_line.json", open(r"E:\luyao\FILE\JMETER\upload_test_line.json", "rb"), "application/json", {})}
        # files=self.files
        response = self.RouteUpload_api.get_routeupload_url(routeName="upload_test_line" , airPortId="" , description="", routeType="2", routeGroup="0", comments="0", substationId="lee0000", fileType="10")
        #response = self.RouteUpload_api.get_routeupload_url (routeName , airPortId , description, routeType, routeGroup, comments, substationId, fileType, files)
        print(response.json())
        #断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("code"))
        self.assertIn("请求成功", response.json().get("msg"))
