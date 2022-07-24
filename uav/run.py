from scripts.test01 import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
from scripts.test02_search import Testsearch
from scripts.test03_list import Testlist

import unittest
import time

#封装测试套件
suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
# suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testsearch))
suite.addTest(unittest.makeSuite(Testlist))

#指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

#文件流形式打开文件
with open(report,"wb") as f:
    #创建HTMLrunner运行器
    runner = HTMLTestRunner(f,title="测试报告")

    #执行测试套件
    runner.run(suite)
