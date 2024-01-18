-- a script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

SELECT
	cities.id,
	cities.name,
	(SELECT name FROM states WHERE id = cities.state_id) AS state_name
	FROM cities
	ORDER BY cities.id;
