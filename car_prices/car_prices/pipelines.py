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
        
        adapter['car_id'] = int(adapter['car_id'])
        adapter['car_mileage'] = int(adapter['car_mileage'])
        adapter['car_engine_power'] = int(adapter['car_engine_power'])
        adapter['car_first_registration'] = int(adapter['car_first_registration'])
        adapter['car_first_registration_month'] = int(adapter['car_first_registration_month'])
        
        month_today = datetime.date.today().year + datetime.date.today().month / 12
        car_month = adapter['car_first_registration'] + adapter['car_first_registration_month'] / 12

        adapter['car_modified'] = datetime.datetime.now(pytz.timezone('Europe/Lisbon'))
        adapter['car_make'] = adapter['car_make'].upper()
        adapter['car_model'] = adapter['car_model'].upper()
        adapter['car_age'] = round(month_today - car_month,2)
        
        created = datetime.datetime.strptime(adapter['car_created'], '%Y-%m-%d %H:%M:%S').astimezone(pytz.timezone('Europe/Lisbon'))
        
        adapter['car_ad_days'] = max((adapter['car_modified'] - created).days, 0)

        return item
