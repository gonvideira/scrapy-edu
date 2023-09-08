"""Modules that allow for working with Scrapy"""
import os
import json
from datetime import date
import time
import scrapy
from scrapy import Request
from car_prices.items import CarItem

class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["www.standvirtual.com"]

    CAR_TYPE = os.environ['TYPE_PARAMETER']
    PAGE = 1
    KM_MIN = 500
    KM_MAX = 125000
    PRICE_MIN = 500
    PRICE_MAX = 100000
    NUMBER_YEARS = 5

    url_current_year = date.today().year
    url_beginning_year = url_current_year - NUMBER_YEARS + 1

    url_query = (
        "https://www.standvirtual.com/graphql?operationName=listingScreen&variables="
        "%7B%22click2BuyExperimentId%22%3A%22%22%2C%22click2BuyExperimentVariant%22%3A%22"
        "%22%2C%22experiments%22%3A%5B%7B%22key%22%3A%22MCTA-900%22%2C%22variant%22%3A%22a"
        "%22%7D%2C%7B%22key%22%3A%22MCTA-1028%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22"
        "key%22%3A%22MCTA-1029%22%2C%22variant%22%3A%22a%22%7D%5D%2C%22filters%22%3A%5B%7B%22"
        F"name%22%3A%22filter_enum_body_type%22%2C%22value%22%3A%22{CAR_TYPE}%22%7D%2C%7B%22name%22%3A%22"
        f"filter_float_first_registration_year%3Ato%22%2C%22value%22%3A%22{url_current_year}%22%7D%2C%7B%22name%22%3A%22"
        f"filter_float_mileage%3Afrom%22%2C%22value%22%3A%22{KM_MIN}%22%7D%2C%7B%22name%22%3A%22"
        f"filter_float_mileage%3Ato%22%2C%22value%22%3A%22{KM_MAX}%22%7D%2C%7B%22name%22%3A%22"
        f"filter_float_price%3Afrom%22%2C%22value%22%3A%22{PRICE_MIN}%22%7D%2C%7B%22name%22%3A%22"
        f"filter_float_price%3Ato%22%2C%22value%22%3A%22{PRICE_MAX}%22%7D%5D%2C%22includeClick2Buy%22%3Afalse%2C%22"
        "includeFiltersCounters%22%3Afalse%2C%22includePriceEvaluation%22%3Atrue%2C%22includePromotedAds%22%3Atrue%2C%22"
        "includeRatings%22%3Afalse%2C%22includeSortOptions%22%3Atrue%2C%22maxAge%22%3A60%2C%22"
        f"page%22%3A{PAGE}%2C%22parameters%22%3A%5B%22origin%22%2C%22make%22%2C%22version%22%2C%22"
        "model%22%2C%22engine_code%22%2C%22fuel_type%22%2C%22gearbox%22%2C%22engine_capacity"
        "%22%2C%22first_registration_month%22%2C%22first_registration_year%22%2C%22"
        f"mileage%22%2C%22engine_power%22%5D%2C%22searchTerms%22%3A%5B%22carros%22%2C%22desde-{url_beginning_year}%22%5D%7D&"
        "extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%2250e3cc18dfb6ea5468e45630696e2e5bd35e7"
        "bc8acc7555bc32419ddececae32%22%2C%22version%22%3A1%7D%7D"
        )

    start_urls = [
        url_query
    ]


    def parse(self, response):
        json_response = json.loads(response.body.decode('utf-8'))
        
        number_cars = json_response['data']['advertSearch']['totalCount']
        cars_page = json_response['data']['advertSearch']['pageInfo']['pageSize']
        number_pages = round(
            number_cars / cars_page + 0.5
        )

        page_counter = 0
        while page_counter < number_pages: # number_pages
            time.sleep(5)
            page_counter += 1
            page_url = (
                "https://www.standvirtual.com/graphql?operationName=listingScreen&variables="
                "%7B%22click2BuyExperimentId%22%3A%22%22%2C%22click2BuyExperimentVariant%22%3A%22"
                "%22%2C%22experiments%22%3A%5B%7B%22key%22%3A%22MCTA-900%22%2C%22variant%22%3A%22a"
                "%22%7D%2C%7B%22key%22%3A%22MCTA-1028%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22"
                "key%22%3A%22MCTA-1029%22%2C%22variant%22%3A%22a%22%7D%5D%2C%22filters%22%3A%5B%7B%22"
                F"name%22%3A%22filter_enum_body_type%22%2C%22value%22%3A%22{self.CAR_TYPE}%22%7D%2C%7B%22name%22%3A%22"
                f"filter_float_first_registration_year%3Ato%22%2C%22value%22%3A%22{self.url_current_year}%22%7D%2C%7B%22name%22%3A%22"
                f"filter_float_mileage%3Afrom%22%2C%22value%22%3A%22{self.KM_MIN}%22%7D%2C%7B%22name%22%3A%22"
                f"filter_float_mileage%3Ato%22%2C%22value%22%3A%22{self.KM_MAX}%22%7D%2C%7B%22name%22%3A%22"
                f"filter_float_price%3Afrom%22%2C%22value%22%3A%22{self.PRICE_MIN}%22%7D%2C%7B%22name%22%3A%22"
                f"filter_float_price%3Ato%22%2C%22value%22%3A%22{self.PRICE_MAX}%22%7D%5D%2C%22includeClick2Buy%22%3Afalse%2C%22"
                "includeFiltersCounters%22%3Afalse%2C%22includePriceEvaluation%22%3Atrue%2C%22includePromotedAds%22%3Atrue%2C%22"
                "includeRatings%22%3Afalse%2C%22includeSortOptions%22%3Atrue%2C%22maxAge%22%3A60%2C%22"
                f"page%22%3A{page_counter}%2C%22parameters%22%3A%5B%22origin%22%2C%22make%22%2C%22version%22%2C%22"
                "model%22%2C%22engine_code%22%2C%22fuel_type%22%2C%22gearbox%22%2C%22engine_capacity"
                "%22%2C%22first_registration_month%22%2C%22first_registration_year%22%2C%22"
                f"mileage%22%2C%22engine_power%22%5D%2C%22searchTerms%22%3A%5B%22carros%22%2C%22desde-{self.url_beginning_year}%22%5D%7D&"
                "extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%2250e3cc18dfb6ea5468e45630696e2e5bd35e7"
                "bc8acc7555bc32419ddececae32%22%2C%22version%22%3A1%7D%7D"
                )
            self.log(page_url)
            yield Request(page_url, callback=self.parse_cars)

    
    
    def parse_cars(self, response):
        json_response = json.loads(response.body.decode('utf-8'))
        cars = json_response['data']['advertSearch']['edges']
        
        for car in cars:
            # item_vehicle = ItemLoader(item=CarItem(), response=response)
            item_vehicle = CarItem()

            item_vehicle['car_id'] = car['node']['id']
            item_vehicle['car_title'] = car['node']['title']
            item_vehicle['car_created'] = car['node']['createdAt']
            item_vehicle['car_shortDescription'] = car['node']['shortDescription']
            item_vehicle['car_url'] = car['node']['url']
            item_vehicle['car_badges'] = car['node']['badges']
            item_vehicle['car_loc_city'] = car['node']['location']['city']['name']
            item_vehicle['car_loc_region'] = car['node']['location']['region']['name']
            item_vehicle['car_price_value'] = car['node']['price']['amount']['units']
            item_vehicle['car_price_currency'] = car['node']['price']['amount']['currencyCode']
            item_vehicle['car_type'] = self.CAR_TYPE

            for dict in car['node']['parameters']:
                if dict['key'] == 'origin':
                    item_vehicle['car_origin'] = dict['displayValue']
                if dict['key'] == 'make':
                    item_vehicle['car_make'] = dict['displayValue']
                if dict['key'] == 'version':
                    item_vehicle['car_version'] = dict['displayValue']
                if dict['key'] == 'model':
                    item_vehicle['car_model'] = dict['displayValue']
                if dict['key'] == 'fuel_type':
                    item_vehicle['car_fuel'] = dict['displayValue']
                if dict['key'] == 'first_registration_year':
                    item_vehicle['car_first_registration'] = dict['value']
                if dict['key'] == 'first_registration_month':
                    item_vehicle['car_first_registration_month'] = dict['value']
                if dict['key'] == 'mileage':
                    item_vehicle['car_mileage'] = dict['value']
                if dict['key'] == 'engine_power':
                    item_vehicle['car_engine_power'] = dict['value']
                if dict['key'] == 'gearbox':
                    item_vehicle['car_transmission'] = dict['value']
                if dict['key'] == 'engine_capacity':
                    item_vehicle['car_engine_capacity'] = dict['value']
                
            yield item_vehicle
