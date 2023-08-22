import sqlite3

db = sqlite3.connect('car_prices/tests.db')
cursor = db.cursor()

# Specify the DDL to a table:
TABLE_DDL = (
    'CREATE TABLE CAR_PRICES ('
    'car_id INT,'
    'car_modified DATETIME,'
    'car_price_value REAL,'
    'car_price_currency TEXT,'
    'FOREIGN KEY (car_id)'
    '   REFERENCES CAR_ADS (car_id)'
    ')'
)

# Call the `cursor.execute` method, passing tbl1_ddl & tbl2_ddl as arguments.
cursor.execute(TABLE_DDL)

# IMPORTANT! Be sure to commit changes you want to persist. Without
# commiting, changes will not be saved.
db.commit()

# Close connection to `sample.db`.
db.close()
