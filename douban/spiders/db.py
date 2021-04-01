import scrapy
from scrapy.http import Request


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']
    header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63",}

    def start_request(self):
        return [Request("https://accounts.douban.com/j/mobile/login/basic",meta={"cookiejar":1},callback=self.parse)]

    def parse(self, response):

        pass
