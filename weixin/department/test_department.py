import datetime
import json
import logging
import time

import pytest
import requests

from weixin.department.token import Weixin


class TestDepartment:
    logging.basicConfig(level=logging.debug)

    @classmethod
    def setup_class(cls):
        Weixin.get_token()
        print(Weixin.token)

    def setup(self):
        print("setup")
        pass

    def test_create(self):
        parentid = 122
        for i in range(10):
            data = {
                "name": "范" + str(parentid),
                "parentid": parentid,
            }

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": Weixin.token},
                              json=data,
                              # proxies={"https": "http://127.0.0.1:8080",
                              #          "http": "http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            logging.debug(r)
            print(r)
            parentid = str(r["id"])
            assert r["errcode"] == 0

    @pytest.mark.parametrize("name", ["中国", "chaina", "중국"])
    def test_crea_name(self, name):
        data = {
            "name": name,
            "parentid": 1
        }

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": Weixin.token},
                          json=data
                          ).json()
        logging.debug(r)

    
    def test_get(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": Weixin.token
                                 }).json()

        logging.info(json.dumps(r, indent=2))
