from scrapy import Spider
from scrapy.http import Request

def product_information(response, attribute):
    """Gets product information from table, for a given attribute"""
    return response.xpath(f'//th[text()="{attribute}"]/following-sibling::td/text()').extract_first()

class BooksSpider(Spider):
    """We are using a spider class that is not the default - CrawlSpider"""
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        """Because we are not using the default spider class, we can use other function names"""
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            book_url = response.urljoin(book)
            yield Request(book_url, callback=self.parse_book)

        next_page = response.xpath('//a[text()="next"]/@href').extract_first()
        next_page_page_url = response.urljoin(next_page)
        yield Request(next_page_page_url, callback=self.parse)
    
    def parse_book(self, response):
        """Function to parse books"""
        book_title = response.xpath('//h1/text()').extract_first()
        book_price = response.xpath('//p[@class="price_color"]/text()').extract_first()
        img_raw = response.xpath('//img/@src').extract_first()
        book_img = img_raw.replace('../..', 'https://books.toscrape.com')
        book_description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()
        book_upc = product_information(response,'UPC')
        book_type = product_information(response,'Product Type')
        book_price_exc = product_information(response,'Price (excl. tax)')
        book_price_inc = product_information(response,'Price (incl. tax)')
        book_tax = product_information(response,'Tax')
        book_availability = product_information(response,'Availability')
        book_num_reviews = product_information(response,'Number of reviews')

        yield {
            'title': book_title,
            'price': book_price,
            'img': book_img,
            'description': book_description,
            'upc': book_upc,
            'type': book_type,
            'price excl': book_price_exc,
            'price incl': book_price_inc,
            'tax': book_tax,
            'availability': book_availability,
            'number reviews': book_num_reviews
        }
