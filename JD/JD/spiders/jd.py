import scrapy
import json
import re
from JD.items import JdItem
class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100009387754&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(i) for i in range(1, 100)]
    def parse(self, response):
        a = json.dumps(response.text)
        b = json.loads(a)
        comment = re.findall(r'{"productAttr":.*}', str(b))
        # json解析
        comm_dict = json.loads(comment[0])
        # comments是评论实体
        comm_list = comm_dict['comments']
        for com in comm_list:
            item = JdItem()
            # 用户id
            item['id'] = com["id"]
            # 名称
            item['name'] = com['referenceName']
            # 用split去空格与换行 join连成整段评论
            item['comment'] = ''.join(com['content'].split())
            # 用户评分
            item['score'] = com['score']  # 用户打分
            # 时间
            item['time'] = com['creationTime']
            yield item



