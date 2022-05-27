select date(created_at) as day , description , count(created_at) as count
from events
where name = 'trained'
group by day , description