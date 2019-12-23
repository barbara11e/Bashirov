SELECT DISTINCT ON
	( tic.trip_id ) pas.first_name,
	pas.last_name,
	pas.mid_name,
	tic.passenger_id,
	COUNT ( tic.passenger_id ) c1 
FROM
	airlines.ticket tic
	JOIN airlines.passenger pas ON tic.passenger_id = pas.passenger_id 
WHERE
	loyality_program_id IS NULL 
	AND tic.passenger_id IS NOT NULL 
	AND tic.trip_id IS NOT NULL 
GROUP BY
	tic.trip_id,
	pas.first_name,
	pas.last_name,
	pas.mid_name,
	tic.passenger_id 
ORDER BY
	c1 DESC;