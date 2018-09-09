# -*- coding: utf-8 -*-
import scrapy
from django_Awesome.items import DjangoAwesomeItem

class DjangoAwesomeSpider(scrapy.Spider):
    name = 'django_awesome'
    # allowed_domains = ['awesome-django.cn']
    start_urls = ['https://www.awesome-django.cn/main.html']

    def parse(self, response):

        full_table = response.xpath("//table[@class=' table table-striped table-hover table-responsive ']/tbody/tr")
        for sel in full_table:
            single_item = DjangoAwesomeItem()
            all_name = sel.xpath("./td[1]/a/text()").extract_first()
            rm_str_name = "".join(all_name.split())
            single_item['name'] = rm_str_name   #去除空格一条龙
            single_item['links'] = sel.xpath("./td[1]/a/@href").extract_first()
            all_star = sel.xpath("./td[2]/text()").extract_first()
            rm_str_star = "".join(all_star.split())
            single_item['star'] = rm_str_star
            all_time = sel.xpath("./td[3]/text()").extract_first()
            rm_str_time = "".join(all_time.split())
            single_item['last_update'] = rm_str_time
            all_descs = sel.xpath("./td[4]/text()").extract_first()
            rm_str_descs = "".join(all_descs.split())
            single_item['detail_descs'] =rm_str_descs
            yield single_item
