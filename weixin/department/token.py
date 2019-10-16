import requests
import yaml
import logging


class Weixin:
    logging.basicConfig(level=logging.DEBUG)
    token = ""

    @classmethod
    def get_token(cls):
        if (len(cls.token)) == 0:
            conf = yaml.safe_load(open("weixin.yaml"))
            logging.debug(conf["evn"])

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                              params={"corpid": conf["evn"]["corpid"],
                                      "corpsecret": conf["evn"]["corpsecret"]}).json()
            cls.token = r["access_token"]
            return cls.token
