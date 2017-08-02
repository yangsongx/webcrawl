# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = ['http://wikipedia.org/']

    def parse(self, response):
        pass
