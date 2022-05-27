select c.customer_id , c.email , count(c.customer_id) as payments_count , cast(sum(p.amount) as float) as total_amount
from customer c
join payment p ON c.customer_id = p.customer_id
group by c.customer_id
order by cast(sum(p.amount) as float) desc
limit 10