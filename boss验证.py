# import time
# t = time.time()
# print(int(round(t * 1000)))
#
#
# url = "https://www.zhipin.com/wapi/zpAntispam/verify/sliderNew"
# p = "IetE43i0RnceRHw1"

import requests
from lxml import etree
import time
class Boss(object):
    def __init__(self):
        self.url = "https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB&city=101010100&industry=&position="
        self.url1 = "https://www.zhipin.com/"
        self.headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'referer': 'https://www.zhipin.com/beijing/?ka=city-sites-101010100',
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        self.proxies = {
    "http": "http://175.42.123.20"

}
    def get_data(self,url):
        res = requests.Session()
        res.get(url=self.url1, headers=self.headers, proxies=self.proxies, timeout=5)
        cookie = res.cookies
        params = {
            'query': '爬虫',
            'city': '101010100'
        }
        resp = res.get(url, headers=self.headers, params=params, cookies=cookie, proxies=self.proxies, timeout=5)
        time.sleep(5)
        print(resp.text, resp.status_code)
        return resp.content
    def parse(self, response):
        html = etree.HTML(response)
        data_list = html.xpath('//*[@id="main"]/div/div[2]/ul/li/div')
        print(data_list)
        item_list = []
        for data in data_list:
            item = {}
            item['name'] = data.xpath('./div[1]/div[1]/div/div[1]/span[1]/a/text()')[0]
            item['money'] = data.xpath('./div[1]/div[1]/div/div[2]/span/text()')[0]
            item['address'] = data.xpath('./div[1]/div[1]/div/div[1]/span[2]/span/text()')[0]
            item['comp'] = data.xpath('./div[1]/div[2]/div/h3/a/text()')[0]
            item['mess'] = data.xpath('./div[1]/div[2]/div/p/text()')[0]
            item['welfare'] = data.xpath('./div[2]/div[2]/text()')[0]
            item_list.append(item)
            time.sleep(5)
        try:
            next_url = 'https://www.zhipin.com/' + str(response.xpath('//div[@class="page"]/a[5]/@href').extract_first())
        except:
            next_url = None
        return item_list, next_url
    def save_data(self,data):
        for i in data:
            print(i)
    def run(self):
        next_url = self.url
        while True:
            data = self.get_data(next_url)
            item_list, next_url = self.parse(data)
            self.save_data(item_list)
            if next_url == None:
                break
if __name__ == '__main__':
    boss = Boss()
    boss.run()












