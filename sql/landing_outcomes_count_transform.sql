SELECT TRIM(UPPER(landing_outcome)) AS standardized_landing_outcome, COUNT(*) AS count
FROM spacextbl
WHERE Date BETWEEN '2010-06-04' AND '2017-03-20'
GROUP BY standardized_landing_outcome
ORDER BY COUNT(*) DESC