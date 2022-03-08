-- This script lists all records of the table second_table.
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- Lists all records.
SELECT score, name
FROM second_table
WHERE name <> 'NULL'
ORDER BY score DESC;
