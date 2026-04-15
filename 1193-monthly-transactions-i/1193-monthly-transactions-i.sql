-- # Write your MySQL query statement below

-- WITH cte1 AS (
--     SELECT 
--         DATE_FORMAT(trans_date, '%Y-%m') AS month,
--         country, 
--         COUNT(*) AS trans_count, 
--         SUM(amount) AS trans_total_amount
--     FROM Transactions 
--     GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
-- ),
-- cte2 AS (
--     SELECT  
--         DATE_FORMAT(trans_date, '%Y-%m') AS month,
--         country,
--         COUNT(*) AS approved_count, 
--         SUM(amount) AS approved_total_amount
--     FROM Transactions
--     WHERE state = 'approved'
--     GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
-- )

-- SELECT 
--     A.month,
--     A.country,
--     A.trans_count,
--     COALESCE(B.approved_count, 0) AS approved_count,
--     A.trans_total_amount,
--     COALESCE(B.approved_total_amount, 0) AS approved_total_amount
-- FROM cte1 A 
-- LEFT JOIN cte2 B 
-- ON A.month = B.month AND A.country = B.country;


SELECT DATE_FORMAT(trans_date,'%Y-%m') as MONTH,
COUNTRY,
COUNT(*) as TRANS_COUNT,
SUM(CASE WHEN state='approved' then 1 else 0 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state='approved' then amount else 0 end) as approved_total_amount
from transactions
group by 
DATE_FORMAT(trans_date,'%y-%m'),
COUNTRY