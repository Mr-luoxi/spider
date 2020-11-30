import requests
import time
import json
from queue import Queue
import threading


# from lxml import etree

class StcokSpider:

    def __init__(self, stock_code, market):
        self.stock_code = stock_code
        # self.start_url = 'http://quote.eastmoney.com/f1.html?code={}&market={}'.format(stock_code, market)
        # self.start_url = 'http://push2ex.eastmoney.com/getStockFenShi?pagesize=144&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wzfscj&pageindex=0&id=6005841&sort=1&ft=1&code=600584&market=1&_=1606196542606'
        # self.start_url = 'http://push2ex.eastmoney.com/getStockFenShi?pagesize=144&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wzfscj&pageindex=2&sort=1&ft=1&code=600584&market=1&_=1606269175713'
        # self.start_url = 'http://push2ex.eastmoney.com/getStockFenShi?pagesize=144&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wzfscj&pageindex=1&sort=1&ft=1&code=600584&market=1&_=1606289374382'
        self.url = 'https://push2.eastmoney.com/api/qt/stock/details/get?secid=1.{}&ut=f057cbcbce2a86e2866ab8877db1d059&fields1=f1,f2,f3,f4,f5&fields2=f51,f52,f53,f54,f55&pos=-150&iscca=1&invt=2&_={}'.format(
            self.stock_code, time.time())
        """
        pagesize：页码
        ut: js的固定参数
        dpt: 固定参数
        pageindex：当前页
        sort：
        ft：
        code:股票代码
        _:日期（可以是一个任意int值）
        :param stock_code:
        :param market:
        """
        self.start_url = 'http://push2ex.eastmoney.com/getStockFenShi?pagesize=144&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wzfscj&pageindex=1&sort=1&ft=1&code=600584&market=1&_={}'.format(
            int(time.time() * 1000))
        self.url_queue = Queue()
        self.html_str_queue = Queue()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

    def parse_url(self, url):
        res = requests.get(url, headers=self.headers)
        return res.content.decode()

    def save_content(self, content_list):
        file_path = self.stock_code + '.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(content_list))

    def run(self):
        print(self.url)
        html_str = self.parse_url(self.url)
        self.save_content(html_str)
        print(html_str)
        pass


if __name__ == '__main__':
    spider = StcokSpider('600584', 2)
    spider.run()
