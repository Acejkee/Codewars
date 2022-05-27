ALTER TABLE USSALES 
add COLUMN location varchar(255)
default 'US';
ALTER TABLE EUSALES 
add COLUMN location varchar(255)
default 'EU';
select *
from ussales
where price>50
UNION ALL
select *
from eusales
where price>50
order by location desc, id;