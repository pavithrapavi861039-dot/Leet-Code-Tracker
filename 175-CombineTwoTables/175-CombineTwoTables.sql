-- Last updated: 7/16/2026, 4:09:15 PM
# Write your MySQL query statement below
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;