select f.name, sum(f.won) as won , sum(f.lost) as lost
from fighters f
JOIN winning_moves m ON f.move_id = m.id
where m.move != 'Hadoken' and move != 'Shouoken' and move != 'Kikoken'
Group by f.name
order by sum(f.won) desc
limit 6