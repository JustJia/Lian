# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    amount = scrapy.Field()
    area = scrapy.Field()
    hm_class = scrapy.Field()
    location = scrapy.Field()
    xiaoqu = scrapy.Field()
    tell = scrapy.Field()
    time = scrapy.Field()
    home_time = scrapy.Field()
