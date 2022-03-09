-- This script lists all cities contained in the database hbtn_0d_usa.
-- Lists all cities.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON state_id = states.id
ORDER BY cities.id ASC;
