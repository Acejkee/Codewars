select date_part('month',payment_date) AS month ,count(p.payment_id) as total_count , sum(p.amount) as total_amount, count(*) filter(where staff_id = 1) as mike_count , sum(amount) filter(where staff_id = 1) as mike_amount, count(*) filter(where staff_id = 2) as jon_count, sum(amount) filter(where staff_id = 2) as jon_amount
from payment p
group by month
order by month