-- Last updated: 7/16/2026, 4:06:43 PM
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;