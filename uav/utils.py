
class Ass:

    def ass1(self,status_code,response):
        a=self.assertEqual(status_code,response.status_code)
        return a
    def ass2(self,code,response):
        b=self.assertEqual(code,response.json().get("code"))
        return b
    def ass3(self,msg,response):
        c=self.assertIn(msg,response.json().get("msg"))
        return c