select date(s.transaction_date) as day, d.name as department , count(s.id) as sale_count
from department d
INNER JOIN sale s ON d.id = s.department_id
group by day , d.name
order by day