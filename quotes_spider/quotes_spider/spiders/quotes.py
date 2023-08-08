import scrapy
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        """Default callback function within the scrapy spider class"""
        item_vehicle = ItemLoader(item=QuotesSpiderItem(), response=response)
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            item_vehicle = ItemLoader(item=QuotesSpiderItem(), response=response)
            
            quote_text = quote.xpath('.//span[@class="text"]/text()').extract_first()
            quote_author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            quote_tags = quote.xpath('.//*[@class="tag"]/text()').extract()

            item_vehicle.add_value('text', quote_text)
            item_vehicle.add_value('author', quote_author)
            item_vehicle.add_value('tags', quote_tags)

            yield item_vehicle.load_item()
        
        next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
        next_url = response.urljoin(next_page)

        yield scrapy.Request(next_url)