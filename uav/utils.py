import json
import unittest
class Ass(unittest.TestCase):
    def get_ass(self,status_code,code,msg,response):

        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(msg, response.json().get("msg"))



