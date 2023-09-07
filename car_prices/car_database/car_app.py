"""Module for working with the database functions"""
from car_database import CarDatabase

db_connection = CarDatabase()

# SETTING UP THE DATABASE
db_connection.create_table_cars()
db_connection.create_table_ads()
db_connection.create_table_prices()

db_connection.update_db('cars.json')

# db_connection.show_all('cars')

db_connection.close_connection()
