-- Last updated: 7/31/2026, 9:32:55 AM
# Write your MySQL query statement below
SELECT 
    r.contest_id,
    ROUND(COUNT(r.user_id) * 100.0 / total.total_users, 2) AS percentage
FROM Register r
CROSS JOIN (
    SELECT COUNT(*) AS total_users FROM Users
) total
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
