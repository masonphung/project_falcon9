SELECT TRIM(mission_outcome) as outcomes, COUNT(mission_outcome) as count
FROM spacextbl
GROUP BY outcomes