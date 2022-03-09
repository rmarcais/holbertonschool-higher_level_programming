-- This script lists all cities contained in the database hbtn_0d_usa.
-- Lists all cities.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON states.id = cities.id
ORDER BY cities.id ASC;
