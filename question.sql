SET search_path TO "happiness";

--Ex A
select s.year, s.country from score_year s
left join (select year, max(score) from score_year group by year) x
on s.year = x.year
where s.score  = x.max
order by s.year


--Ex B
select year, round(avg(score),2) from score_year
group by year
order by year

--Ex C

SELECT t.year, t.country, t.rank FROM (
SELECT
    year,
    country,
    RANK () OVER (
        PARTITION BY year
        ORDER BY score DESC
    ) rank
FROM score_year) t
WHERE t.country = 'Portugal'
GROUP BY t.year, t.country, t.rank
ORDER BY t.year


--Ex D
--1 (Higher GDP)
select s.year, round(avg(s.score),2) from score_year s
inner join (select c.name, c.gdp from country c order by c.gdp desc limit 10) x
on s.country=x.name
group by s.year
order by s.year

--2 (Lower GDP)
select s.year, round(avg(s.score),2) from score_year s
inner join (select c.name, c.gdp from country c order by c.gdp asc limit 10) x
on s.country=x.name
group by s.year
order by s.year

--3 (Higher infant mortality)
select s.year, round(avg(s.score),2) from score_year s
inner join (select c.name, c.infant_mortality from country c order by c.infant_mortality desc limit 10) x
on s.country=x.name
group by s.year
order by s.year

--4 (Higher literacy)

select s.year, round(avg(s.score),2) from score_year s
inner join (select c.name, c.literacy from country c order by c.literacy desc limit 10) x
on s.country=x.name
group by s.year
order by s.year

--Ex E

--1(larger improvement)
select s1.country, (s2.score-s1.score) as improvement from score_year s1
inner join score_year s2
on s1.country = s2.country
where s1.year = 2015 and s2.year=2019
order by improvement desc
limit 3

--2(larger regression)
select s1.country, (s2.score-s1.score) as improvement from score_year s1
inner join score_year s2
on s1.country = s2.country
where s1.year = 2015 and s2.year=2019
order by improvement 
limit 3
