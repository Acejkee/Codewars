select race , count(race) as count
from demographics
group by race
order by count(race) desc