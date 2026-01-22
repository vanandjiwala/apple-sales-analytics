SELECT
store_id,
store_name,
city,
country,
NOW() as created_timestamp
FROM
{{ref("bronze_stores")}}