select count(producer) as count_products_types , producer
from products
group by producer
order by count_products_types desc , producer asc