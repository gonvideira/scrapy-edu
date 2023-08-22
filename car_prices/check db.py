import sqlite3

db = sqlite3.connect('car_prices/tests.db')
cursor = db.cursor()

# Query to select all records from TABLE:
SQL = "SELECT * FROM CAR_PRICES"

cursor.execute(SQL)

headers = [ii[0] for ii in cursor.description]

for header in headers:
    print(header)

for record in cursor:
    print(record)

# Close connection to `sample.db`.
db.close()
