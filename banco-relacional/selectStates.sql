select * from states

select 
    Acronym,
    name as "States Name"
from states
where regions = "South"

select 
    Name,
    Regions,
    Population
from states
where population >= 10
order by population desc