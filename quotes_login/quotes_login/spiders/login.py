import scrapy
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath('//input[@name="csrf_token"]/@value').extract_first()
        yield FormRequest(
            'https://quotes.toscrape.com/login',
            formdata={
                'csrf_token': csrf_token,
                'username': 'foobar',
                'password': 'foobar'
            },
            callback=self.parse_with_login
        )
    
    def parse_with_login(self, response):
        if response.xpath('//a[text()="Logout"]'):
            self.log('You logged in!')
