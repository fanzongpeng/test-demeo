import time

import requests

from weixin.department.token import Weixin


class TestUser:
    department = 173

    @classmethod
    def setup_class(cls):
        pass

    def create_user(self):
        uuid = time.time()
        data = {"userid": "fan"+uuid,
                "name": "",
                "department": "",
                "mobile": ""}
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.token},
                          json=data
                          )
