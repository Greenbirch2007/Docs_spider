# -*- coding: utf-8 -*-
import scrapy
from Flask1_docs.items import Flask1DocsItem


class FlaskDocsSpider(scrapy.Spider):
    name = 'flask_docs'
    allowed_domains = ['dormousehole.readthedocs.io']
    start_urls = ['https://dormousehole.readthedocs.io/en/latest/']

    def parse(self, response):

        screams  =response.xpath("//div[@class='toctree-wrapper compound']/ul/li")

        for sel in screams:
            docs_item = Flask1DocsItem()

            docs_item['content'] = sel.xpath("./a/text()").extract_first()
            all_links = sel.xpath("./a/@href").extract_first()
            docs_item['links'] = 'https://dormousehole.readthedocs.io/en/latest/' + all_links

            yield docs_item