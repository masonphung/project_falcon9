SELECT customer, SUM(payload_mass) AS total_payload_mass
FROM spacextbl
WHERE Customer = 'NASA (CRS)'
GROUP BY Customer