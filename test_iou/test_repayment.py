import json
import logging
import requests
import jsonpath


class TestRepayment(object):
    logging.basicConfig(level=logging.INFO)

    def test_iou(self):
        r = requests.post('http://59.110.219.71:9113/ioucenter/repay/queryTradeResult',
                          headers={'Content-Type': 'application/json'},
                          json={
                              "head": {
                                  "transType": "T",
                                  "transDate": "2019-08-20",
                                  "transTime": "18:25",
                                  "transSerialNo": "21321312312323",
                                  "sysCode": "1350"
                              },

                              "body": {
                                  "orderNo": "5010201909250615018520001093",

                              }

                          }
                          )
        logging.info(r.url)
        logging.info(json.dumps(r.json(), indent=4))
        ##assert jsonpath.jsonpath(r.json(), '$.result.tradeResultList[*].transactionNo' = "5050201909262019136730130502")

