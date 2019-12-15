--SELECT count(passenger_id) from passenger

--SELECT count(*) from trip

--SELECT setval('airlines.loyality_program_seq', 1, true);
--SELECT setval('airlines.trip_seq', 1, true);

--SELECT count(*) from trip

-- В таблицу путешествия добавить айди рейса по его названию
-- UPDATE airlines.trip
-- SET flight_id=f.flight_id
-- from airlines.flight f
-- WHERE trip.flight_number=f.flight_number

--SELECT setval('airlines.ticket_seq', 1, true);

-- Boarding_data - ticket
-- INSERT into ticket(first_name, middle_name, last_name, birth_date, flight_date, flight_time, flight_number, booking_code, ticket_number)
-- SELECT first_name, middle_name, last_name, birth_date, flight_date, flight_time, flight_number, booking, ticket_num from boarding_csv
-- 
-- Select count(*) from ticket

-- В таблицу билета добавить айди пассажира по его имени, фамилии, отчеству и дате рождения (уникальное сочетание)
-- UPDATE airlines.ticket
-- SET passenger_id=p.passenger_id
-- from airlines.passenger p
-- WHERE ticket.passenger_id is NULL and ticket.first_name=p.first_name and ticket.last_name=p.last_name --and ticket.middle_name=p.mid_name --and ticket.birth_date=p.birth_date

-- Select * from ticket
-- where passenger_id is null
 
--В таблицу билета добавить айди путешествия по его номеру, дате и времени
-- UPDATE airlines.ticket
-- SET trip_id=t.trip_id
-- from airlines.trip t
-- WHERE ticket.trip_id is NULL and ticket.flight_number=t.flight_number and ticket.flight_date=t.trip_date --and ticket.flight_time=t.trip_time

-- SELECT * FROM ticket
-- where trip_id = '6291888'

-- SELECT * from ticket
-- WHERE trip_id is NULL

-- SELECT * from trip
-- where trip_date = '2017-05-04' and flight_number= 'SU1441'

-- Select * from trip
-- where trip_date = '2017-01-01' and trip_time ='07:15:00'

-- Delete from trip
-- where trip_id<100000

-- Select * from trip
-- where flight_id = 3482
-- order by trip_date

--TRUNCATE trip CASCADE


--PointzAggregator-AirlinesData - ticket
-- INSERT into ticket(first_name, last_name,  flight_date, flight_number, fare, loyalty)
-- SELECT first,  last,  flight_date, flight_number, fare, number from airlines."PointzAggregator_AirlinesData" --p , loyality_program l, fare f
-- where fare_id=f.fare_id and f.fare_code=p.Fare and loyality_program_id=l.loyality_program_id and p.number=l.loyality_card

-- FrequentFlyer - ticket
-- INSERT into ticket(first_name, last_name,  flight_date, flight_number, loyalty)
-- SELECT firstname,  lastname,  date, flight, (program || ' ' || programnumber) from airlines."FrequentFlyerForumProfilesChangedDate" -- f, loyality_program l
-- where loyality_program_id=l.loyality_program_id and (program || ' ' || programnumber)=l.loyality_card

-- Конкатенация столбцов
-- Select program || ' ' || programnumber from airlines."FrequentFlyerForumProfilesChangedDate"

--В таблицу билета добавить никнейм тем, у кого нет имени
-- UPDATE airlines.ticket t
-- SET first_name=f.nickname
-- from airlines."FrequentFlyerForumProfilesChangedDate" f, loyality_program l
-- WHERE t.first_name is NULL and l.loyality_program_id=t.loyality_program_id and (program || ' ' || programnumber)=l.loyality_card

-- Select * from fare
-- where fare_code = 'JGRPGN0PC'

-- DELETE
-- FROM
-- airlines.fare USING airlines.fare f
-- WHERE
-- fare.fare_code = f.fare_code AND fare.fare_id > f.fare_id;

-- Sirena - ticket
-- INSERT into ticket(first_name, last_name, middle_name, birth_date,  flight_date, flight_number, loyalty, fare, ticket_number)
-- SELECT paxfirstname,  paxlastname, paxmiddlename, paxbirthdate, departdate, flight, ff, farebaggage, code_e_ticket from airlines."SERENAChangedDate" 
-- WHERE NOT EXISTS (select * from ticket)
--where fare_id=f.fare_id and f.fare_code=s.farebaggage and loyality_program_id=l.loyality_program_id and s.ff=l.loyality_card

--select count(*) from ticket

--TRUNCATE fare CASCADE


-- Skyteam
-- INSERT into ticket(flight_date, flight_number, loyalty, fare)
-- SELECT date, flight, ff, fare from airlines."SkyTeam_Exchange"



-- YourBoarding
-- INSERT into ticket(last_name, first_name, flight_date, flight_time, flight_number, loyalty, ticket_number, booking_code)
-- SELECT last_name, first_name, date, time, flight, ff, e_ticket, pnr from airlines."YourBoardingPassDotAeroChangedDate"


--Добавить в билет айди на программу лояльности по номеру программы лояльности
-- UPDATE airlines.ticket
-- SET loyality_program_id=l.loyality_program_id
-- from airlines.loyality_program l
-- WHERE ticket.loyalty=l.loyality_card

-- Добавить айди еды по коду в билет
-- UPDATE airlines.ticket
-- SET food_id=f.food_id
-- from airlines.food f, airlines."SERENAChangedDate" s
-- WHERE f.code=s.meal and s.code_e_ticket=ticket.ticket_number


-- Добавить айди агрегатора по названию агрегатора в билет
-- UPDATE airlines.ticket
-- SET aggregator_id=a.aggregator_id
-- from airlines.aggregator a, airlines."SERENAChangedDate" s
-- WHERE a.name=s.agentinfo and s.code_e_ticket=ticket.ticket_number
