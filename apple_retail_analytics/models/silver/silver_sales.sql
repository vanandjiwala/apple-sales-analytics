SELECT 
sale_id,
sale_date,
store_id,
product_id,
quantity,
NOW() as created_timestamp
FROM {{ref("bronze_sales")}}