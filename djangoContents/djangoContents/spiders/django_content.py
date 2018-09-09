# -*- coding: utf-8 -*-
import scrapy
from djangoContents.items import DjangocontentsItem

class DjangoContentSpider(scrapy.Spider):
    name = 'django_content'
    allowed_domains = ['docs.djangoproject.com']
    start_urls = ['https://docs.djangoproject.com/zh-hans/2.0/contents/']

    def parse(self, response): #还是整理模块解析的有问题
        all_table = DjangocontentsItem()
        all_table['name']= response.xpath("//li[@class='toctree-l1']/ul/li/ul/li/a/text()").extract_first()
        yield all_table
        # all_conent = response.xpath("//div[@id='docs-content']/div")
        # for sel in all_conent:
        #
        #     full_name = sel.xpath("./div/ul/li/ul/li/ul/li/a").extract()
        #     for item_i in full_name:
        #         full_table = DjangocontentsItem()
        #         full_table['name'] = item_i.xpath("./text()")
        #         full_table['links'] = item_i.xpath("./@href")
            # full_links  = sel.xpath("./div/ul/li/ul/li/ul/li/a/@href").extract()
            # for item_l in full_links:
            #     full_table = DjangocontentsItem()
            #
            #     full_table['links'] = item_l[3:]



#4-5个层次最好使用正则处理！