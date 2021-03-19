import requests
from lxml import etree
import json
class douban:
    def __init__(self, j):
        self.url = 'https://movie.douban.com/top250?start=' + str(j)
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        }
    def ceshi(self):
        res = requests.get(url=self.url, headers=self.headers)
        html = res.text
        #print(html)
        data_list = etree.HTML(html).xpath('//*[@class="info"]')
        for data in data_list:
            movie = {"name": data.xpath('./div[1]/a/span[1]/text()'), "message": data.xpath('normalize-space(./div[2]/p[1]/text())'), "Introduction": data.xpath('./div[2]/p[2]/span/text()')}
            print(movie)


if __name__ == '__main__':
    for i in range(10):
        j = i * 25
        Douban = douban(j)
        Douban.ceshi()