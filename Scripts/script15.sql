SELECT
	flight_id,
	flight_number,
	airport_departure_id,
	airport_arrival_id,
	a1.airport_name,
	a2.airport_name 
FROM
	flight f
	LEFT JOIN airport a1 ON a1.airport_id = f.airport_arrival_id
	LEFT JOIN airport a2 ON a2.airport_id = f.airport_departure_id 
WHERE
	airport_arrival_id = airport_departure_id