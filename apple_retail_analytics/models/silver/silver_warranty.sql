SELECT
claim_id,
claim_date,
sale_id,
repair_status,
NOW() as created_timestamp
FROM
{{ref("bronze_warranty")}}