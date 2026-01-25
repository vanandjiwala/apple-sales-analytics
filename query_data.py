import duckdb

query = """
SELECT 
s.sale_id,
s.sale_date,
s.store_id,
ss.store_name,
ss.city,
ss.country,
p.product_name,
p.launch_date,
p.price,
p.category_name,
w.claim_id,
w.claim_date,
w.repair_status
FROM silver_sales s
LEFT JOIN silver_products p ON s.product_id = p.product_id
LEFT JOIN silver_sites ss ON s.store_id = ss.store_id
LEFT JOIN silver_warranty w ON w.sale_id = s.sale_id
"""

# 
# 

with duckdb.connect('data/apple-retail.db') as con:
    print(con.sql(query=query).df())

# 10  silver_products
# 11     silver_sales
# 12     silver_sites
# 13  silver_warranty