SELECT landing_outcome, COUNT(landing_outcome) AS count
FROM spacextbl
WHERE Date BETWEEN '2010-06-04' AND '2017-03-20'
GROUP BY landing_outcome
ORDER BY Count DESC