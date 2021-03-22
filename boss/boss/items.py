# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    money = scrapy.Field()
    address = scrapy.Field()
    comp = scrapy.Field()
    mess = scrapy.Field()
    welfare = scrapy.Field()



