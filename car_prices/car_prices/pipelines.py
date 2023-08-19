# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
from itemadapter import ItemAdapter
import pytz

class CarPricesPipeline:
    
    def process_item(self, item, spider):
        """Adding a column with modified date and time"""
        adapter = ItemAdapter(item)
        adapter['car_modified'] = datetime.datetime.now(pytz.timezone('Europe/Lisbon'))
        adapter['car_make'][0] = adapter['car_make'][0].upper()
        adapter['car_age'] = datetime.date.today().year - adapter['car_first_registration'][0]

        return item
