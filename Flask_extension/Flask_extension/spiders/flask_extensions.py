# -*- coding: utf-8 -*-
import scrapy
from Flask_extension.items import FlaskExtensionItem


class FlaskExtensionsSpider(scrapy.Spider):
    name = 'flask_extensions'
    allowed_domains = ['http://flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/extensions/']

    def parse(self, response):
        all_conent = response.xpath("//div[@class='extension']")# 此处是全部内容，所以不用解析
        for sel in all_conent:
            exten_item = FlaskExtensionItem()
            exten_item['name']= sel.xpath("./h2/text()").extract_first()
            # all_descs = sel.xpath("div[@class='description']/p[1]").extract_first()  #尝试加入re正则，是在提取的部分
            #  描述过于复杂，如果要解决，用这则即可，但是为了保持项目的整体性，暂时做减法

            # exten_item['author']= sel.xpath("./dl/dd[1]/text()").extract_first()
            exten_item['PI_page']= sel.xpath("./dl/dd[2]/a/@href").extract_first()
            exten_item['docs']= sel.xpath("./dl/dd[3]/a/@href").extract_first()
            exten_item['on_github']= sel.xpath("./dl/dd[4]/a/@href").extract_first()


            yield exten_item

