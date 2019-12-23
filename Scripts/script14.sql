WITH subselect AS (
	SELECT DISTINCT ON
		( T.passenger_id, T.loyality_program_id, t2.passenger_id, t2.loyality_program_id ) T.passenger_id,
		T.loyality_program_id 
	FROM
		ticket
		T LEFT JOIN loyality_program l USING ( loyality_program_id )
		LEFT JOIN ticket t2 ON ( l.loyality_program_id = t2.loyality_program_id ) 
	WHERE
		T.passenger_id IS NOT NULL 
		AND t2.passenger_id IS NOT NULL 
		AND T.loyality_program_id IS NOT NULL 
		AND t2.passenger_id != T.passenger_id 
		AND t2.ticket_id != T.ticket_id 
	ORDER BY
		T.loyality_program_id 
	) SELECT COUNT
	( loyality_program_id ) count_rows,
	loyality_program_id 
FROM
	subselect 
GROUP BY
	loyality_program_id 
HAVING
	COUNT ( loyality_program_id ) > 2 
ORDER BY
	count_rows;