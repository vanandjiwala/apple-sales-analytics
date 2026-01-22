SELECT 
p.product_id,
p.product_name,
p.category_id,
p.launch_date,
CAST(p.price as FLOAT) as price,
COALESCE(c.category_name, 'Not Available') as category_name,
NOW() as created_timestamp
FROM {{ref("bronze_products")}} p
JOIN {{ref("bronze_category")}} c ON c.category_id = p.category_id