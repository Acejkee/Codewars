select date(created_at) as date , count(date(created_at)) as count , sum(count(date(created_at))) over (order by date(created_at))::int as total
from posts
group by date(created_at)
order by date