'''
Extracting URLs of the books in Page 1 of the site given...
'''
# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
# for Chrome Webdriver
from scrapy.selector import Selector
# helps in gathering URLS 
from scrapy.http import Request


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self): # returns request
        self.driver = webdriver.Chrome('F:\\Setups\\chromedriver_win32\\chromedriver.exe')
        # Driver path 
        self.driver.get('http://books.toscrape.com')
        # site to get

        sel = Selector(text=self.driver.page_source)
        # making selector object and getting Page Source
        books = sel.xpath('//h3/a/@href').extract()
        # all books URLs
        for book in books:
            url = 'http://books.toscrape.com/' + book
            # absolute URL
            yield Request(url, callback=self.parse_book)
            # generating values

    def parse_book(self, response):
        pass
