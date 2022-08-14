# import time
# from time import  strftime,gmtime
# a={"a":11}
# b={"b":22}
#
# k =["%s"%(a),"%s"%(b)]
# print(k)
# report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# name = "移动巡检{}".format(strftime("%Y%m%d-%H%M%S"))
# print(name)

from bs4 import  BeautifulSoup
from utils import init_log_config
import logging
html = """ <html>
 <head>
 <title>测试报告</title>
 </head>
 <body>
  <p id="test01">软件测试</p>
   <p id="test02">测试软件</p>
    <a href="/api.html">接口测试</a>
     <a href="/web.html">Web自动化测试</a>
      <a href="/app.html">APP自动化测试</a>
       </body>
        </html> """

soup = BeautifulSoup(html,"html.parser")
#获取P的对象
# print(soup.p)
#获取第一个p标签id属性的值
# print(soup.p["id"])
#获取第一个p标签的标签名称
# print(soup.p.string)
init_log_config()

#获取所有P标签
# print(soup.find_all("p"))

data= {}
for s in soup.find_all("p"):
    # print("id={} name={}".format(s["id"],s.string))
    data.setdefault(s["id"], s.string)

logging.info("response is {}".format(data))
print(data)

