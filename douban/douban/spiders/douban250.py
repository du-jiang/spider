import scrapy
from douban.items import DoubanItem

class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        data_list = response.xpath('//*[@class="info"]')
        for data in data_list:
            item = DoubanItem()
            item['name'] = data.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['message'] = data.xpath('normalize-space(./div[2]/p[1]/text())').extract_first()
            item['score'] = data.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['Introduction'] = data.xpath('./div[2]/p[2]/span/text()').extract_first()
            yield item
        url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if url != None:
            url = response.urljoin(url)
            yield scrapy.Request(url=url)
