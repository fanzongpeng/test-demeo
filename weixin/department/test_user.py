import logging
import time
import pystache

import requests


from weixin.department.token import Weixin
from weixin.department.user import user


class TestUser:
    department = 173

    @classmethod
    def setup(cls):
        print(".......................................")

    def test_create_user(self):
        uuid = str(time.time()).replace(".", "")[:11]
        data = {"userid": "fan" + uuid,
                "name": "fan" + uuid,
                "department": self.department,
                "email": uuid + "@qq.com"
                }
        r=user().userapi(data)

        logging.debug(r)
        print(r)

    def test_getuser_float(self):
        f = "".join(open("creatuser.json", encoding="utf - 8").readlines())
        uuid = str(time.time()).replace(".", "")[:11]
        ##logging.debug(self.get_user({"userid": "zhangsan", "name": "fan"+uuid, "mobile": uuid}))
        data= user().get_user(f, {"usrid": "zhangsan", "name": "范"+uuid, "mobile": uuid})
        data=data.encode("utf-8")
        r = user().userapi1(data)
        logging.debug(r)

        



    def test_user_float1(self):
        print(pystache.render("hello {{name}} {{vale}} ",
                              {"name": "范睿羿",
                               "vale": "hahah"}))
