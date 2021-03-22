# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class BossPipeline:
    def __init__(self):
        self.file = open('boss.txt', 'w')
    def process_item(self, item, spider):
        #将字典数据进行数据化
        json_data = json.dumps(item, ensure_ascii=False) + ',\n'
        #将数据写入文件
        self.file.write(json_data)
        #将数据返回给引擎
        return item
    def __del__(self):
        self.file.close()