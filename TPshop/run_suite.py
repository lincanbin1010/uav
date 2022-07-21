import time
import unittest

from scripts.test01_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
#封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

#指定测试报告路径
#report = "./report/report.html"
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

#文件流形式打开文件


with open(report,"wb") as f:
    #创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f,title="tpshop-report")

    #执行测试套件
    runner.run(suite)