打开文件：open



读取json文件的方法
import json
f=open("readme.json",“r”,encodeing="utf8")
data =json.load(f)
f.close()

写入JSON文件
import json data = {'name': 'tom', 'age': 20, 'country': '中国'} f = open('temp.json', 'w', encoding='UTF-8') json.dump(data, f, ensure_ascii=False) # ensure_ascii=False 代表中文不转义 f.close()

fixture

