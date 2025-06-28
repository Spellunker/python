select 
    s.name as State, 
    c.name as City, 
    regions as Region 
from states s, cities c
where s.id = c.id_state

select
    c.name as City,
    s.name as State,
    regions as Region
from states s
inner join cities c
    on s.id = c.id_state