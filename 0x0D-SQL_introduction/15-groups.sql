-- This script lists the number of records with the same score in the table second_table.
-- Lists the number of records.
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
