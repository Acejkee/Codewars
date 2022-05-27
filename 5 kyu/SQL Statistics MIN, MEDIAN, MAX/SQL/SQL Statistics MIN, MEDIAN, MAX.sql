select min(score) as min, cast(round((sum(score) / count(score)),0) as float)  as median , max(score) as max
from result 