SELECT e.name Enterprise, c.name City
from enterprises e, companies_unities cu, cities c
where e.id = cu.city_id and c.id = cu.city_id
and headquarter