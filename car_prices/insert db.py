import json
import sqlite3

db = sqlite3.connect('car_prices/tests.db')
cursor = db.cursor()



SQL = (
    'INSERT INTO CAR_PRICES (car_id, car_modified, car_price_value, car_price_currency) '
    'VALUES (:car_id, :car_modified, :car_price_value, :car_price_currency)'
)

cursor.executemany(SQL, json.load(open('car_prices/cars_simple.json', 'r', encoding='utf-8')))

db.commit()

for record in cursor:
    print(record)

# Close connection to `sample.db`.
db.close()
