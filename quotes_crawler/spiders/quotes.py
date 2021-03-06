# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
				for quote in response.xpath('//div[@class="quote"]'):
						yield {
								"text": quote.xpath('.//span[@class="text"]/text()').extract_first(),
								"author": quote.xpath('.//small[@class="author"]/text()').extract_first(),
								"tags": quote.xpath('.//a[@class="tag"]/text()').extract()
						}

				url = response.xpath('//li[@class="next"]/a/@href').extract_first()
				next_url = response.urljoin(url)
				
				yield scrapy.Request(url=next_url, callback=self.parse)
