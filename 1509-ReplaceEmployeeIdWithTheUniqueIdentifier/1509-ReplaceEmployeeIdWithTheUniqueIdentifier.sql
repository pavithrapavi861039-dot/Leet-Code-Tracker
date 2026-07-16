-- Last updated: 7/16/2026, 4:04:40 PM
# Write your MySQL query statement below
SELECT 
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id;