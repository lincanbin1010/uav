#导包
import time
import unittest
from scripts.test01_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
#组装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

#指测试定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#打开文件流
with open(report,"wb") as f:

#创建HTMLrunner运行器
    runner = HTMLTestRunner(f, title="API report")
#执行测试套件
    runner.run(suite)