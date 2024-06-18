-- List the number of records with the same score, labeled as 'number', and sort by this count descending
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;

