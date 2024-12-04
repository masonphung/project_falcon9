SELECT DISTINCT booster_version, landing_outcome
FROM spacextbl
WHERE landing_outcome = 'Success' AND (payload_mass BETWEEN 4000 AND 6000)