-- Last updated: 7/16/2026, 4:06:09 PM
# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;