select id , name , split_part(characteristics,',',1) as characteristic
from monsters
ORDER BY ID;