drop database teste;
create database teste;

CREATE TABLE if not exists teste.public.raizen (
	year_month date NULL,
	uf varchar NULL,
	product varchar NULL,
	unit varchar NULL,
	volume float8 NULL
);

