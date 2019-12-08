create schema airlines; 
set search_path TO airlines;
create sequence passenger_seq start 1;
create table passenger (
	passenger_id integer default nextval('passenger_seq') primary key,
	first_name varchar not null,
	last_name varchar not null,
	mid_name varchar,
	sex varchar,
	birth_date date,
	doc_number varchar not null
);

comment on column passenger.first_name is 'Имя пассажира';
comment on column passenger.last_name is 'Фамилия пассажира';
comment on column passenger.mid_name is 'Отчество пассажира';
comment on column passenger.sex is 'Пол';
comment on column passenger.birth_date is 'Дата рождения';
comment on column passenger.doc_number is 'Номер документа';

create sequence airplane_seq start 1;
create table airplane (
	airplane_id integer default nextval('airplane_seq') primary key,
	airplane_number varchar not null,
	airplane_name varchar not null
)
;
comment on column airplane.airplane_number is 'Номер самолета';
comment on column airplane.airplane_name is 'Наименование самолета';

 create SEQUENCE airport_seq start 1;
 create table airport(
	airport_id integer default nextval('airport_seq') primary key,
	airport_name varchar not null,
	airport_country varchar not null,
	airport_city varchar not null
 )
 ;
 comment on column airport.airport_name is 'Наименование аэропорта';
 comment on column airport.airport_country is 'Страна аэропорта';
 comment on column airport.airport_city is 'Город аэропорта';


create sequence flight_seq start 1;
create table flight (
	flight_id integer default nextval('flight_seq') primary key,
	flight_number varchar, 
	airport_departure_id integer references airport (airport_id),
	airport_arrival_id integer  references airport (airport_id), 
	flight_date date,
	time_departure timestamp,
	time_arrival timestamp,
	code_share varchar,
	airplane_id integer references airplane (airplane_id)
)
;
 comment on column flight.flight_number is 'Номер рейса';
 comment on column flight.airport_departure_id is 'Аэропорт отправления';
 comment on column flight.airport_arrival_id is 'Аэропорт отправления';
 comment on column flight.flight_date is 'Дата рейса';
 comment on column flight.time_departure is 'Время отправления';
 comment on column flight.time_arrival is 'Время прибытия';
 comment on column flight.code_share is 'Кодшер?';
 comment on column flight.airplane_id is 'Тип самолета';


create sequence fare_seq start 1;
create table fare (
	fare_id integer default nextval('fare_seq') primary key,
	fare_code varchar
);
comment on column fare.fare_code is 'Код тарифа';

CREATE SEQUENCE  loyality_program_seq start 1;
CREATE TABLE  loyality_program (
	loyality_program_id integer default nextval('loyality_program_seq') primary key,
	loyality_card varchar,
	loyality_program_name varchar
)
;
comment on column loyality_program.loyality_card is 'Номер бонусной карты';
comment on column loyality_program.loyality_program_name is 'Наименование программы';

CREATE SEQUENCE  food_seq start 1;
CREATE TABLE  food (
	food_id integer default nextval('food_seq') primary key,
	code varchar,
	name varchar	
)
;
comment on column food.code is 'Код';
comment on column food.name is 'Наименование (расшировка)';


CREATE SEQUENCE  aggregator_seq start 1;
CREATE TABLE  aggregator (
	aggregator_id integer default nextval('aggregator_seq') primary key,
	name varchar,
	properties varchar	
)
;
comment on column aggregator.name is 'Наименование агрегатора/сайта';
comment on column aggregator.properties is '+ некоторые полезные характеристик сайта, которые мы можем найти вне наших данных';

CREATE SEQUENCE ticket_seq start 1;

CREATE TABLE  ticket (
	ticket_id integer default nextval('ticket_seq') primary key,
	passenger_id integer references passenger (passenger_id),
	flight_id integer references flight (flight_id),
	loyality_program_id integer references loyality_program (loyality_program_id),
	fare_id integer references fare (fare_id),
	food_id integer references food (food_id),
	aggregator_id integer references aggregator (aggregator_id)
)
;
comment on column ticket.passenger_id is 'Пассажир';
comment on column ticket.flight_id is 'Рейс';
comment on column ticket.loyality_program_id is 'Программа бонусная';
comment on column ticket.fare_id is 'Тариф';
comment on column ticket.food_id is 'Еда';
comment on column ticket.aggregator_id is 'Агрегатор';




