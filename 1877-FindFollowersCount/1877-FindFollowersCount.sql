-- Last updated: 7/31/2026, 9:32:48 AM
# Write your MySQL query statement below
SELECT 
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;