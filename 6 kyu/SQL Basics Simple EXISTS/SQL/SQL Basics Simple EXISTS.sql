select id , name
from departments
where EXISTS (select price from sales where departments.id = sales.department_id and price > 98.000);