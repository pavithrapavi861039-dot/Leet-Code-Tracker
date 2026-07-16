-- Last updated: 7/16/2026, 4:06:51 PM
# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m
ON e.id = m.managerId;