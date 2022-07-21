#封装被测试系统接口
class LoginApi:
#初始化
    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        #self.url_verify = "http://localhost/index.php/Home/user/login.html"
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
        #self.url_login="http://localhost/index.php/Home/user/login.html"
#获取验证码
    def get_verify_code(self,session):
        return session.get(self.url_verify)
#登录
    def get_url_login(self,session):
        login_data={
            "username" : username ,
            "password" : password ,
            "verify_code" : verify_code
        }
        return session.post(url=self.url_login,data=login_data)