select capital
from countries
where country like 'E%' and (continent = 'Afrika' or continent = 'Africa') 
order by capital
limit 3