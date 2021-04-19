# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class JdPipeline:
    def __init__(self):
        self.file = open('jd.txt', 'w')
    def open_spider(self, spider):
        print("爬虫开始")
    def process_item(self, item, spider):
        for k, v in item.items():
            shuju = str(k) + ":" + str(v) + "\n"
            self.file.write(shuju)
        #将数据返回给引擎
        return item
    def close_spider(self, spider):
        self.file.close()
        print("爬虫结束")
