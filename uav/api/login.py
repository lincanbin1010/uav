#封装被测试系统接口
class LoginApi:
#初始化
    def __init__(self):
        self.url_login = "http://192.168.1.93:7080/api/v2/login"

#登录
    def get_url_login(self,session,username,password,verify_code):
        login_data={
            "username" : username ,
            "password" : password ,
            "verify_code" : verify_code
        }
        return session.post(url=sel
        f.url_login,data=login_data)