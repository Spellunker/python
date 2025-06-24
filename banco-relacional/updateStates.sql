update states
set name = "Maranhão"
where acronym = "MA"

select est.name from states est
where acronym = "MA"

update states
set name = "Paraná",
    population = 11.32
where acronym = "PR"

update states
set id = id - 3
where id >=7

select * from states