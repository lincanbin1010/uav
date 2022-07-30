#导包
import unittest

import parameterized

from api.routeupload import routeuploadApi



#构造数据
# def build_data():
#     file ="./data/login.json"
#     test_data =[]
#     with open(file,encoding="utf-8") as f:
#         json_data = json.load(f)  # 加载JSON文件数据
#         for case_data in json_data:
#             username = case_data.get("username")
#             password = case_data.get("password")
#             vcode = case_data.get("vcode")
#             status_code = case_data.get("status_code")
#             code = case_data.get("code")
#             msg = case_data.get("msg")
#             test_data.append((username, password, vcode, status_code, code, msg))
#             print(test_data)
#     return test_data

#创建测试类
class Testrouteload(unittest.TestCase):
    def setUp(self):
        self.routeupload_api = routeuploadApi()

    # @parameterized.expand(build_data())

    #调用文件上传接口
    def test07_routeload_1(self):
        # files = {"file": ("upload_test_line.json", open("E:\luyao\FILE\JMETER\upload_test_line.json", "rb"), "application/json", {})}
        self.routeName ="upload_test_line"
        routeName =self.routeName
        self.airPortId = ""
        airPortId=self.airPortId
        self.description = ""
        description=self.description
        self.routeType = "2"
        routeType=self.routeType
        self.routeGroup = "0"
        routeGroup=self.routeGroup
        self.comments = ""
        comments=self.comments
        self.substationId = "lee0000"
        substationId=self.substationId
        self.fileType = "10"
        fileType=self.fileType
        # response = self.routeupload_api.get_routeupload_url(routeName="upload_test_line", airPortId="", description="", routeType="2", routeGroup="0", comments="", substationId="lee0000", fileType="10")

        response = self.routeupload_api.get_routeupload_url(routeName , airPortId , description, routeType, routeGroup, comments, substationId, fileType)
        print(response.json())
        #断言
        self.assertEqual("200", response.status_code)
        self.assertEqual("1", response.json().get("code"))
        self.assertIn("请求成功", response.json().get("msg"))
