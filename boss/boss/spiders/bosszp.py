import scrapy
from requests import Request

from boss.items import BossItem

class BosszpSpider(scrapy.Spider):
    name = 'bosszp'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=%E7%88%AC%E8%99%AB&ka=sel-city-100010000']

    def parse(self, response):
        data_list = response.xpath('//div[@class="job-primary"]')
        for data in data_list:
            item = BossItem()
            item['name'] = data.xpath('./div[1]/div[1]/div/div[1]/span[1]/a/text()').extract_first()
            item['money'] = data.xpath('./div[1]/div[1]/div/div[2]/span/text()').extract_first()
            item['address'] = data.xpath('./div[1]/div[1]/div/div[1]/span[2]/span/text()').extract_first()
            item['comp'] = data.xpath('./div[1]/div[2]/div/h3/a/text()').extract_first()
            item['mess'] = data.xpath('./div[1]/div[2]/div/p/text()').extract_first()
            item['welfare'] = data.xpath('./div[2]/div[2]/text()').extract_first()
            yield item
        url = 'https://www.zhipin.com/' + str(response.xpath('//div[@class="page"]/a[5]/@href').extract_first())
        if url != None:
            url = response.urljoin(url)
            yield scrapy.Request(url=url)

    # def start_requests(self):
    #     for i in self.start_urls:
    #         yield Request(i, meta={
    #             'dont_redirect': True,
    #             'handle_httpstatus_list': [302]
    #         }, callback=self.parse)