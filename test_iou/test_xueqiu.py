import json
import logging

import jsonpath
import requests


class Test_requests(object):
    url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json'
    logging.basicConfig(level=logging.INFO)

    def test_xueqiu_quote(self):
        params = {'_t': '1UNKNOWNc60715cb4a61425b311034a49f4aa024.3446260779.1563002521424.1563005246620',
                  '_s': '8c6b2d',
                  'category': '1',
                  'pid': -1,
                  'size': 10000,
                  'x': 1.3,
                  'page': 1}

        headers = {'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
                  'User-Agent': 'Xueqiu Android 11.19',
                  'Host': 'stock.xueqiu.com'}

        cookies = {'xq_a_token': '5806a70c6bc5d5fb2b00978aeb1895532fffe502', 'u': '3446260779'}
        response = requests.get(self.url, params=params, headers=headers, cookies=cookies)
        logging.info(json.dumps(response.json(), indent=2))
        assert jsonpath()
