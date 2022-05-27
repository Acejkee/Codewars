select title
from film_actor fa
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film f ON fa.film_id = f.film_id
where fa.actor_id in (105,122)
group by f.title having count(*) = 2
order by f.title