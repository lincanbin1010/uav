from scripts.test01 import TestLogin
# from tools.HTMLTestRunner import HTMLTestRunner
from tools.HTMLTestRunner_PY3 import HTMLTestRunner
from scripts.test02_search import Testsearch
from scripts.test04_list import Testlist
from scripts.test03_save import Testsave
from scripts.test05_update import Testupdate
from scripts.test06_delete import Testdelete
from scripts.test07_routeupload import Testrouteload
from scripts.test08_searchroutid import TestSearchrouteid
from scripts.test11_routeupdate import Testrouteupdate
from scripts.test12_complexRoute import TestcomplexRoute
from scripts.test13_predictFlyData import TestpredictFlyData
from scripts.test14_uavtasksave import Testuavtasksave
from scripts.test_postman import Testpostman
from scripts.test_tasksearch import TestTaskSearch
from scripts.test10_takeoffsave import Testtakeoffsave


import unittest
import time

import logging
from utils import init_log_config

#测试用例批量封装
# suite = unittest.TestLoader().discover("./scripts/","test01.py")

# 封装测试套件
suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(Testsearch))
# suite.addTest(unittest.makeSuite(Testsave))
# suite.addTest(unittest.makeSuite(Testlist))
# suite.addTest(unittest.makeSuite(Testupdate))
# suite.addTest(unittest.makeSuite(Testdelete))
# suite.addTest(unittest.makeSuite(Testrouteload))
suite.addTest(unittest.makeSuite(TestSearchrouteid))
suite.addTest(unittest.makeSuite(Testrouteupdate))
suite.addTest(unittest.makeSuite(TestcomplexRoute))
suite.addTest(unittest.makeSuite(TestpredictFlyData))
suite.addTest(unittest.makeSuite(Testuavtasksave))
# suite.addTest(unittest.makeSuite(Testpostman))
# suite.addTest(unittest.makeSuite(TestTaskSearch))
# suite.addTest(unittest.makeSuite(Testtakeoffsave))

#指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

#文件流形式打开文件
with open(report,"wb") as f:
    #创建HTMLrunner运行器
    runner = HTMLTestRunner(f,title="测试报告")

    #执行测试套件
    runner.run(suite)

    init_log_config()
    logging.info("info")
    logging.error("error")
    logging.debug("debug")

