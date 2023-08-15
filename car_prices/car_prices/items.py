# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field

class CarItem(Item):
    """Car item to be used in cars spider"""
    # define the fields for your item here like:
    car_id = Field()
    car_title = Field()
    car_created = Field()
    car_shortDescription = Field()
    car_url = Field()
    car_badges = Field()
    car_loc_city = Field()
    car_loc_region = Field()
    car_price_value = Field()
    car_price_currency = Field()
    car_origin = Field()
    car_make = Field()
    car_version = Field()
    car_model = Field()
    car_fuel = Field()
    car_first_registration = Field()
    car_mileage = Field()
    car_engine_power = Field()
