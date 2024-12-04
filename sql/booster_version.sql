%%sql
SELECT DISTINCT booster_version, payload_mass
FROM spacextbl
WHERE payload_mass IN (
    SELECT MAX(payload_mass)
    FROM spacextbl
)