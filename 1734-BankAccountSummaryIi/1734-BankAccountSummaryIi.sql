-- Last updated: 7/31/2026, 9:32:57 AM
# Write your MySQL query statement below
SELECT 
    u.name,
    SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t
    ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;