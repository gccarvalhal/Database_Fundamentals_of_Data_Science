
--criar base de dados
-- CREATE DATABASE happiness;

--criar schema
CREATE SCHEMA happiness;

--selecionar o uso deste banco de dados
SET search_path TO "happiness";

--criar tabelas
CREATE TABLE country(
    name VARCHAR(255)  PRIMARY KEY,
    population INTEGER,
    area INTEGER,
    infant_mortality REAL,
    gdp REAL,
    literacy NUMERIC(5,2)
);

CREATE TABLE score_year(
    country VARCHAR(255) REFERENCES country(name),
    year INTEGER ,
    score NUMERIC(5,2),
    PRIMARY KEY(country, year)
);