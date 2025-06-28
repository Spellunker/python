SELECT * FROM mayors;
SELECT * FROM cities;

SELECT * from cities c inner join mayors m on c.id = m.city_id;
SELECT * from cities c left outer join mayors m on c.id = m.city_id;
SELECT * from cities c right outer join mayors m on c.id = m.city_id;
-- SELECT * from cities c full join mayors m on c.id = m.city_id; erro por não suportar o full join

SELECT * from cities c left outer join mayors m on c.id = m.city_id
union -- all traz as duplicadas
SELECT * from cities c right outer join mayors m on c.id = m.city_id;