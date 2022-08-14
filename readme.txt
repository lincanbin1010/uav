打开文件：open

token：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

读取json文件的方法
import json
f=open("readme.json",“r”,encodeing="utf8")
data =json.load(f)
f.close()

写入JSON文件
import json data = {'name': 'tom', 'age': 20, 'country': '中国'} f = open('temp.json', 'w', encoding='UTF-8') json.dump(data, f, ensure_ascii=False) # ensure_ascii=False 代表中文不转义 f.close()

fixture
git push timeout test

调用request的get/post方法来发送数据，如果是multi-part多消息体数据，传递参数的方法 response = session.post(self.url,data=data,files={'x':'y'})

from bs4 import Beautifulsoup
soup = BeautifulSoup(open("index.html"）,"html.parser")  #open文件名方式
soup = BeautifulSoup("<html>data</html>","html.parser")   #openHTML字符串内容



