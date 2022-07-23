#封装被测试系统接口
import app


class LoginApi:
#初始化
    def __init__(self):
        self.url_login = app.BASE_URL+"/api/v2/index/login"

#登录
    def get_url_login(self,session,username,password,vcode):
        login_data={
            "username" : username ,
            "password" : password ,
            "vcode" : vcode
        }
        return session.post(url=self.url_login,data=login_data)