# -*- coding: utf-8 -*-
import scrapy
from django_module.items import DjangoModuleItem


class DjangoModulesSpider(scrapy.Spider):
    name = 'django_modules'
    allowed_domains = ['docs.djangoproject.com']
    start_urls = ['https://docs.djangoproject.com/zh-hans/2.0/py-modindex/']

    def parse(self, response):
        all_content = response.xpath("//div[@role='main']/ul/")
        for sel in all_content:
            full_item = DjangoModuleItem()

            full_item['name']=sel.xpath("./li/a/tt/text()").extract_first()
            yield full_item