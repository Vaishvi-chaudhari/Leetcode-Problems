# Write your MySQL query statement below
-- 1. Find Employees with salary < 30000
-- 2. Select only those emp for which m_id NOT EXISTS IN e_id.
SELECT employee_id
FROM Employees
WHERE salary < 30000
AND manager_id NOT IN (
    SELECT employee_id 
    FROM Employees
)
ORDER BY employee_id;