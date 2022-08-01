--Extra

--Criar uma view

CREATE VIEW Rank_CPLP as
SELECT t.year, t.country, t.rank FROM (
SELECT
    year,
    country,
    RANK () OVER (
        PARTITION BY year
        ORDER BY score DESC
    ) rank
FROM score_year) t
WHERE t.country in( 'Portugal','Angola', 'Brazil','Cape Verde', 'Guinea-Bissau', 'Equatorial Guinea', 'Mozambique','Sao Tome & Principe', 'East Timor')
GROUP BY t.year, t.country, t.rank
ORDER BY  t.country,t.year;