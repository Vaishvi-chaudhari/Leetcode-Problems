# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id # If id is odd and is last seat then no swap.
        WHEN id % 2 = 1 THEN id+1 # If odd then swap with next (even) seat
        ELSE id-1 # If Even then swap with prev (odd) seat
    END AS id, student
FROM Seat
ORDER BY id;