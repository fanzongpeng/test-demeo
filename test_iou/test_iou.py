import json
import logging
import requests
import jsonpath

from test_iou.iouapi import Iouapi


class TestRepayment(object):
    logging.basicConfig(level=logging.INFO)

    def test_iou(self):

        data=data
        r = Iouapi().create_iou(data)
        logging.info(r.url)
        logging.info(json.dumps(r.json(), indent=4))
        ##assert jsonpath.jsonpath(r.json(), '$.result.tradeResultList[*].transactionNo' = "5050201909262019136730130502")
