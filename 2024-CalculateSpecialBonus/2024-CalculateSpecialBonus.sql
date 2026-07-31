-- Last updated: 7/31/2026, 9:32:40 AM
# Write your MySQL query statement below
SELECT 
    employee_id,
    CASE 
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' 
        THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id;