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
p.category_name
FROM {{ ref('silver_sales') }} s
LEFT JOIN {{ ref('silver_products') }} p ON s.product_id = p.product_id
LEFT JOIN {{ ref('silver_sites') }} ss ON s.store_id = ss.store_id
LEFT JOIN {{ ref('silver_warranty') }} w ON w.sale_id = s.sale_id