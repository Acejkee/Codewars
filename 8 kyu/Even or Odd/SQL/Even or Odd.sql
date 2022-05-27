select number ,
case when abs(number) % 2 = 1 then 'Odd'
when abs(number) % 2 = 0 then 'Even'
end as is_even
from numbers