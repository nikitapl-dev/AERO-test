create schema aero;
create table aero.canabis_data(
	id text,
	uid text,
	strain text,
	cannabinoid_abbreviation text,
	cannabinoid text,
	terpene text,
	medical_use text,
	health_benefit text,
	category text,
	type text,
	buzzword text,
	brand text,
	json_data jsonb,
	date_insert timestamp default now()
);