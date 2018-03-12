# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Lian.items import LianItem
from scrapy_redis.spiders import RedisCrawlSpider
class LianSpider(RedisCrawlSpider):
    name = 'lian'
    # allowed_domains = ['lianjia.com']
    # start_urls = ['http://bj.lianjia.com/']
    redis_key = 'lian'
    rules = (
        #  城市url
        Rule(LinkExtractor(allow=r'https://[a-z]{2,3}\.lianjia\.com/$'), callback='get_url', follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'ershoufang/\d+\.html$'), callback='home_list', follow=True),
        # 翻页
        Rule(LinkExtractor(allow=r'/ershoufang/pg\d+/$'), follow=True),
    )

    def __init__(self,*args,**kwargs):
        domain = kwargs.pop('domain','')
        self.allowed_domain = list(filter(None,domain.split(',')))
        super(LianSpider, self).__init__(*args,**kwargs)

    def get_url(self, response):
        city_url = response.url + 'ershoufang/'
        yield scrapy.Request(url=city_url)

    def home_list(self,response):
        # print(response.url)
        item = LianItem()
        item['title'] = response.xpath('/html/body/div[3]/div/div/div[1]/h1/text()').extract_first()
        item['price'] = response.xpath('//div[@class="text"]/div/span/text()').extract_first() + response.xpath(
            '//div[@class="text"]/div/span/i/text()').extract_first()
        item['amount'] = response.xpath('/html/body/div[5]/div[2]/div[2]/span[1]/text()').extract_first() + '万'
        item['area'] = response.xpath('//div[@class="area"]/div[1]/text()').extract_first()
        item['tell'] = '-'.join(response.xpath('/html/body/div[5]/div[2]/div[5]/div/div[3]/text()').extract())
        item['hm_class'] = response.xpath('//div[@class="base"]/div[2]/ul/li[1]/text()').extract_first()
        item['location'] = ''.join(response.xpath('//div[@class="areaName"]/span[2]/a/text()').extract())
        item['xiaoqu'] = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        item['home_time'] = response.xpath('//div[@class="base"]/div[2]/ul/li[12]/text()').extract_first()
        # print(item)
        yield item