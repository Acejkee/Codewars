select p.pokemon_name as pokemon_name , p.str * m.multiplier as modifiedStrength , m.element 
from pokemon p 
JOIN multipliers m ON p.element_id = m.id 
where p.str * m.multiplier >= 40 
order by p.str desc