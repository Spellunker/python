select
    regions as "Region",
    sum(population) as Total
from states
group by regions
order by Total desc

select
    sum(population) as Total
from states

select
    avg(population) as Total
from states
