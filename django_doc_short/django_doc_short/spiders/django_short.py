# -*- coding: utf-8 -*-
import scrapy
from django_doc_short.items import DjangoDocShortItem

class DjangoShortSpider(scrapy.Spider):
    name = 'django_short'
    allowed_domains = ['docs.djangoproject.com']
    start_urls = ['https://docs.djangoproject.com/zh-hans/2.0/']

    def parse(self, response):
        all_cotent = response.xpath("//ul[@class='simple']/li")
        full_item = DjangoDocShortItem()
        for sel in all_cotent:
            full_item['name'] =sel.xpath("./a/span[@class='doc']/text()").extract_first()
            change_link = sel.xpath(".//a[@class='reference internal']/@href").extract_first()
            str_link = 'https://docs.djangoproject.com/zh-hans/2.0/' + str(change_link)
            full_item['links'] =str_link
            yield full_item