import json
import time
import scrapy
from scrapy import Request

class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["www.standvirtual.com"]
    url_page = 1
    url_query = f'https://www.standvirtual.com/graphql?operationName=listingScreen&variables=%7B%22click2BuyExperimentId%22%3A%22%22%2C%22click2BuyExperimentVariant%22%3A%22%22%2C%22experiments%22%3A%5B%7B%22key%22%3A%22MCTA-900%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22key%22%3A%22MCTA-1028%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22key%22%3A%22MCTA-1029%22%2C%22variant%22%3A%22a%22%7D%5D%2C%22filters%22%3A%5B%7B%22name%22%3A%22filter_enum_body_type%22%2C%22value%22%3A%22city-car%22%7D%2C%7B%22name%22%3A%22filter_float_first_registration_year%3Ato%22%2C%22value%22%3A%222022%22%7D%2C%7B%22name%22%3A%22filter_float_mileage%3Ato%22%2C%22value%22%3A%2275000%22%7D%5D%2C%22includeClick2Buy%22%3Afalse%2C%22includeFiltersCounters%22%3Afalse%2C%22includePriceEvaluation%22%3Atrue%2C%22includePromotedAds%22%3Atrue%2C%22includeRatings%22%3Afalse%2C%22includeSortOptions%22%3Atrue%2C%22maxAge%22%3A60%2C%22page%22%3A{url_page}%2C%22parameters%22%3A%5B%22origin%22%2C%22make%22%2C%22version%22%2C%22model%22%2C%22engine_code%22%2C%22fuel_type%22%2C%22first_registration_month%22%2C%22first_registration_year%22%2C%22mileage%22%2C%22engine_power%22%5D%2C%22searchTerms%22%3A%5B%22carros%22%2C%22desde-2018%22%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%2250e3cc18dfb6ea5468e45630696e2e5bd35e7bc8acc7555bc32419ddececae32%22%2C%22version%22%3A1%7D%7D'
    
    def start_requests(self):
        """Function that makes first requests to car gallery pages""" 
        return [
            Request(self.url_query, callback=self.parse)
        ]

    def parse(self, response):
        json_response = json.loads(response.body.decode('utf-8'))
        self.log(f'URL PAGE IS: {self.url_page}')

        cars = json_response['data']['advertSearch']['edges']
        for car in cars:
            car_url = car['node']['url']
            yield Request(car_url, callback=self.parse_car)
        
        pages = json_response['data']['advertSearch']['pageInfo']['pageSize']
        if pages > self.url_page:
            time.sleep(30)
            self.url_page += 1
            yield Request(self.url_query, callback=self.parse)
    
    def parse_car(self, response):
        raw_title = response.xpath('//div[@class="offer-header__row hidden-xs visible-tablet-up"]/h1/text()').extract()
        car_title = ' '.join(raw_title).strip()
        yield {
            'title': car_title
        }
