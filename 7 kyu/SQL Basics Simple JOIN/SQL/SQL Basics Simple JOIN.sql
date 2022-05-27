select p.id , p.name , p.isbn , p.company_id , p.price , c.name as company_name
from products p
LEFT JOIN companies c ON p.company_id = c.id