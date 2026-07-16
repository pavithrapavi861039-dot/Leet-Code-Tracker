-- Last updated: 7/16/2026, 4:06:07 PM
# Write your MySQL query statement below
SELECT 
    CASE
        WHEN id % 2 = 1 AND id + 1 <= (SELECT COUNT(*) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;