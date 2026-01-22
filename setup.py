import duckdb

## Local Development
conn = duckdb.connect('data/apple-retail.db')

## Cloud Development - Uncomment for setting up data in motherduck warehouse
# conn = duckdb.connect('md:apple-retail')

response = conn.sql("SHOW TABLES")

print("Initial State")
print("*" * 25)
print(response.df())
print("*" * 25)

create_category_sql = f"""
CREATE OR REPLACE TABLE category AS
SELECT *
FROM
read_csv_auto('data/category.csv', normalize_names = True)
"""
conn.sql(create_category_sql)

create_products_sql = f"""
CREATE OR REPLACE TABLE products AS
SELECT *
FROM
read_csv_auto('data/products.csv', normalize_names = True)
"""
conn.sql(create_products_sql)

create_sales_sql = f"""
CREATE OR REPLACE TABLE sales AS
SELECT *
FROM
read_csv_auto('data/sales.csv', normalize_names = True)
"""
conn.sql(create_sales_sql)

create_stores_sql = f"""
CREATE OR REPLACE TABLE stores AS
SELECT *
FROM
read_csv_auto('data/stores.csv', normalize_names = True)
"""
conn.sql(create_stores_sql)

create_warranty_sql = f"""
CREATE OR REPLACE TABLE warranty AS
SELECT *
FROM
read_csv_auto('data/warranty.csv', normalize_names = True)
"""
conn.sql(create_warranty_sql)

response = conn.sql("SHOW TABLES")

print("Initial State")
print("*" * 25)
print(response.df())
print("*" * 25)

conn.close()