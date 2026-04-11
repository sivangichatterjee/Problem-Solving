# Write your MySQL query statement below
-- Select x.salary as SecondHighestSalary 
-- from
-- (select salary, 
-- rank() over(order by salary desc) as rnk 
-- from Employee)x where x.rnk=2


SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
