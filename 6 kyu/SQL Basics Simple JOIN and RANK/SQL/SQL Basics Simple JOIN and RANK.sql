select p.id, p.name, count(s.sale) as sale_count , RANK ( ) OVER ( PARTITION BY p.id ORDER BY p.id DESC) AS sale_rank
from people p
JOIN sales s ON p.id = s.people_id
group by p.id