select t.id,t.heads, b.legs,t.arms,b.tails,
case 
when t.heads > t.arms then 'BEAST'
when b.tails > b.legs then 'BEAST'
else 'WEIRDO'
end as species
FROM top_half t
JOIN bottom_half b on t.id = b.id
order by species