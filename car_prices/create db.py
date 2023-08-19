import sqlite3

db = sqlite3.connect('car_prices/tests.db')
cursor = db.cursor()

# Specify the DDL to a table:
TABLE_DDL = """CREATE TABLE CAR_PRICES (
                car_id                  INT,
                car_title               TEXT,
                car_created             DATETIME,
                car_modified            DATETIME,
                car_shortDescription    TEXT,
                car_url                 TEXT,
                car_loc_city            TEXT,
                car_loc_region          TEXT,
                car_price_value         REAL,
                car_price_currency      TEXT,
                car_make                TEXT,
                car_version             TEXT,
                car_model               TEXT,
                car_fuel                TEXT,
                car_first_registration  INT,
                car_age                 INT,
                car_mileage             INT,
                car_engine_power        INT
                )"""

# Call the `cursor.execute` method, passing tbl1_ddl & tbl2_ddl as arguments.
cursor.execute(TABLE_DDL)

# IMPORTANT! Be sure to commit changes you want to persist. Without
# commiting, changes will not be saved.
db.commit()

# Close connection to `sample.db`.
db.close()
