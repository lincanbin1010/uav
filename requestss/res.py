import  requests


#发送请求
response = requests.get("http://www.baidu.com")
response.encoding = "utf-8"
print(response.encoding)
print(response.text)