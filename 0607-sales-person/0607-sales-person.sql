# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders AS o
    JOIN Company AS c
    ON o.com_id = c.com_id
    WHERE o.sales_id = s.sales_id
    AND c.name = 'RED'
);