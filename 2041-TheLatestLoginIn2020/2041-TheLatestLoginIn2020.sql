-- Last updated: 7/31/2026, 9:32:39 AM
# Write your MySQL query statement below
SELECT 
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;