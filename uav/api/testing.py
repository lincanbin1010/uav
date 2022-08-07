import time
from time import  strftime,gmtime
a={"a":11}
b={"b":22}

k =["%s"%(a),"%s"%(b)]
print(k)
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
name = "移动巡检{}".format(strftime("%Y%m%d-%H%M%S"))
print(name)