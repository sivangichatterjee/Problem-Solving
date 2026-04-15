# Write your MySQL query statement below
select m.name from
employee e join employee m
on e.managerId=m.id
group by m.name, m.id
having count(*)>=5
-- having count(*)>=5