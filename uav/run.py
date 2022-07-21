from scripts.test01_db import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

import unittest
import  time

#封装测试套件
suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

#指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

#文件流形式打开文件
with open(report,"wb") as f:
    #创建HTMLrunner运行器
    runner = HTMLTestRunner(f,title="测试报告")

    #执行测试套件
    runner.run(suite)
