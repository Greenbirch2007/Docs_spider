# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DjangoAwesomeItem(scrapy.Item):
    name = scrapy.Field()
    links = scrapy.Field()
    star = scrapy.Field()
    last_update = scrapy.Field()
    detail_descs = scrapy.Field()