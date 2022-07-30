import requests

url = "http://183.6.112.146:7080/api/v2/inspectionRoute/json"

payload={'routeName': 'upload_test_line',
'airPortId': '',
'description': '',
'routeType': '2',
'routeGroup': '0',
'comments': '',
'substationId': 'lee0000',
'fileType': '10'}
files=[
  ('file',('upload_test_line.json',open(r"E:\luyao\FILE\JMETER\upload_test_line.json",'rb'),'application/json'))
]
headers = {
  'Access-Token': 'AD073973000342D8AB428F3EE1EF0726',
  'Cookie': 'JSESSIONID=EE6C52DD30E95476F030FB54DA9BBFA1'
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.text)