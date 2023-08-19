import json
import sqlite3

db = sqlite3.connect('car_prices/cars.db')
cursor = db.cursor()

# Specify the DDL to a table:
TABLE_DDL = """CREATE TABLE CAR_PRICES (
              car_id   INT,
              car_title TEXT,
              car_created  DATETIME,
              car_shortDescription  TEXT,
              car_url  TEXT,
              car_loc_city  TEXT,
              car_loc_region  TEXT,
              car_price_value  REAL,
              car_price_currency  TEXT,
              car_make  TEXT,
              car_version  TEXT,
              car_model  TEXT,
              car_fuel  TEXT,
              car_first_registration  INT,
              car_mileage  INT,
              car_engine_power  INT,
              car_modified  DATETIME)"""

"""# Call the `cursor.execute` method, passing tbl1_ddl & tbl2_ddl as arguments.
cursor.execute(TABLE_DDL)

# IMPORTANT! Be sure to commit changes you want to persist. Without
# commiting, changes will not be saved.
db.commit()

# Close connection to `sample.db`.
db.close()"""


cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
names = [description[0] for description in cursor.description]

for name in names:
    print(name)

db.close()

"""newegg_json = json.load(open('newegg_scrapy.json'))

columns = []
column = []
for data in newegg_json:
    column = list(data.keys())
    for col in column:
        if col not in columns:
            columns.append(col)

value = []
values = []
for data in newegg_json:
    for i in columns:
        value.append(str(dict(data).get(i)))
    values.append(list(value))
    value.clear()

create_query = 'create table if not exists table_newegg (model, item, price)'
insert_query = 'insert into table_newegg values (?,?,?)'
c = conn.cursor()
c.execute(create_query)
c.executemany(insert_query, values)
conn.commit()
c.close()"""