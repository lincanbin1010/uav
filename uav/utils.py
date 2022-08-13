import os,time
import logging
from logging import handlers

#定义公共断言方法
def get_ass(self,status_code,code,msg,response):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(msg, response.json().get("msg"))

#日志输出方法
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#初始化日志配置
def init_log_config():
    #1、初始化日志对象
    logger = logging.getLogger()
    #2、设置日志级别
    logger.setLevel(logging.INFO)
    #3、创建控制台日志处理器和文件日志处理器
    sh = logging.StreamHandler()

    logfile = BASE_DIR + os.sep + "log" + os.sep + "uav{}.log".format(time.strftime("%Y%m%d-%H%M%S"))
    fh = logging.handlers.TimedRotatingFileHandler(logfile,when='H',interval=12,backupCount=5,encoding='UTF-8')
    #4、设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    #5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)