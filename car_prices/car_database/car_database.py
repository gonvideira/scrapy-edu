"""Module for working with SQLite databases"""
import sqlite3
import json

class CarDatabase():
    """Class to hold functions for the car database"""
    db_connection = sqlite3.connect('car_database/car_database.db')
    db_cursor = db_connection.cursor()

    def create_table_cars(self):
        """Create the cars table"""
        query_string = (
            """
                CREATE TABLE cars (
                car_id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
                car_make TEXT,
                car_model TEXT,
                car_version TEXT,
                car_transmission TEXT,
                car_fuel TEXT,
                car_engine_power INTEGER,
                car_engine_capacity INTEGER,
                car_type TEXT,
                UNIQUE (car_make,car_model,car_version,car_transmission)
                )
            """
        )
        self.db_cursor.execute(query_string)
        self.db_connection.commit()
        print('Database table CARS created successfully!')

    def create_table_ads(self):
        """Create the ads table"""
        query_string = (
            """
                CREATE TABLE ads (
                car_id INT, 
                car_ad_id INT PRIMARY KEY,
                car_ad_title TEXT,
                car_ad_created TEXT,
                car_ad_modified TEXT,
                car_ad_days INT,
                car_ad_shortDescription TEXT,
                car_ad_url BLOB,
                car_ad_badges BLOB,
                car_ad_loc_region TEXT,
                car_ad_loc_city TEXT,
                car_ad_price_value INT,
                car_ad_price_currency TEXT,
                car_ad_year INT,
                car_ad_month INT,
                car_ad_age REAL,
                car_ad_mileage INT,
                car_ad_warranty INT,
                car_ad_origin TEXT,
                FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
                )
            """
        )
        self.db_cursor.execute(query_string)
        self.db_connection.commit()
        print('Database table ADS created successfully!')

    def create_table_prices(self):
        """Create the prices table"""
        query_string = (
            """
                CREATE TABLE prices (
                car_ad_id INT,
                car_modified TEXT,
                car_price_value INT,
                FOREIGN KEY (car_ad_id) REFERENCES ads(car_ad_id) ON DELETE CASCADE
                )
            """
        )
        self.db_cursor.execute(query_string)
        self.db_connection.commit()
        print('Database table PRICES created successfully!')

    def add_cars(self,json_file):
        """Function that ads records to key tables from json file"""
        with open(json_file, 'r', encoding='utf-8') as file:
            json_string = json.load(file)
            for record in json_string:
                if 'car_version' not in record:
                    record['car_version'] = 'not available'
                if 'car_transmission' not in record:
                    record['car_transmission'] = 'not available'
                if 'car_engine_capacity' not in record:
                    record['car_engine_capacity'] = 'not available'
                self.db_cursor.execute(
                    'INSERT OR IGNORE INTO cars ('
                    'car_make, car_version, car_model, car_fuel, car_engine_power, '
                    'car_engine_capacity, car_transmission, car_type'
                    ') '
                    'VALUES ('
                    ':car_make, :car_version, :car_model, :car_fuel, :car_engine_power, '
                    ':car_engine_capacity, :car_transmission, :car_type'
                    ')',
                    record
                )
        print('Record CARS added to Database!')
        self.db_connection.commit()

    def add_car_ads(self,json_file):
        """Function that ads car ads"""
        with open(json_file, 'r', encoding='utf-8') as file:
            json_string = json.load(file)
            for record in json_string:
                if 'car_version' not in record:
                    record['car_version'] = 'not available'
                if 'car_transmission' not in record:
                    record['car_transmission'] = 'not available'
                if 'car_engine_capacity' not in record:
                    record['car_engine_capacity'] = 'not available'
                if 'car_origin' not in record:
                    record['car_origin'] = 'not available'
                if 'car_badges' not in record:
                    record['car_warranty'] = 'no warranty'
                    record['car_badges'] = 'not available'
                elif 'WARRANTY' in record['car_badges']:
                    record['car_warranty'] = 'warranty'
                    record['car_badges'] = ';'.join(record['car_badges'])
                else:
                    record['car_warranty'] = 'no warranty'
                    record['car_badges'] = ';'.join(record['car_badges'])

                self.db_cursor.execute(
                    'INSERT OR REPLACE INTO ads ('
                    'car_id, car_ad_id, car_ad_title, car_ad_created, car_ad_modified, '
                    'car_ad_days, car_ad_shortDescription, car_ad_url, '
                    'car_ad_loc_region, car_ad_loc_city, car_ad_price_value, '
                    'car_ad_price_currency, car_ad_year, car_ad_month, '
                    'car_ad_age, car_ad_mileage, car_ad_origin, car_ad_warranty, car_ad_badges'
                    ') '
                    'VALUES ('
                    '(SELECT car_id FROM cars WHERE car_make = :car_make '
                    'AND car_model = :car_model AND car_version  = :car_version '
                    'AND car_transmission = :car_transmission),'
                    ':car_id, :car_title, :car_created, :car_modified, '
                    ':car_ad_days, :car_shortDescription, :car_url, '
                    ':car_loc_region, :car_loc_city, :car_price_value, '
                    ':car_price_currency, :car_first_registration, :car_first_registration_month, '
                    ':car_age, :car_mileage, :car_origin, :car_warranty, :car_badges'
                    ')',
                    record
                )
        print('Record ADS added to Database!')
        self.db_connection.commit()

    def add_car_prices(self,json_file):
        """Function to add prices to the prices table"""
        with open(json_file, 'r', encoding='utf-8') as file:
            json_string = json.load(file)
            for record in json_string:
                self.db_cursor.execute(
                    'INSERT INTO prices ('
                    'car_ad_id, car_modified, car_price_value'
                    ') '
                    'VALUES ('
                    ':car_id, :car_modified, :car_price_value'
                    ')',
                    record
                )       
        print('Record PRICES added to Database!')
        self.db_connection.commit()

    def update_db(self,json_file):
        """Function that calls the functions to update the database"""
        self.add_cars(json_file)
        self.add_car_prices(json_file)
        self.add_car_ads(json_file)
        print('Database updated!')

    def show_all(self, table_name):
        """Show all records"""
        query_string = f'SELECT * FROM {table_name}'
        self.db_cursor.execute(query_string)
        records = self.db_cursor.fetchall()
        for record in records:
            print(record)


    def close_connection(self):
        """Needed to invoke close connection"""
        self.db_connection.close()
        print('Connection to database closed!')
