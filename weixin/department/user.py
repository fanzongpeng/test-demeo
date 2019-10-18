import pystache
import requests

from weixin.department.token import Weixin


class user():

    def userapi(self, data):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=data
                          ).json()

        return r
    def userapi1(self,data):
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          headers={"Content-Type": "application/json"},
                          data=data
                          ).json()
        return r

    def get_user(self, f, dict):

        ## print(f)
        return pystache.render(f, dict)

