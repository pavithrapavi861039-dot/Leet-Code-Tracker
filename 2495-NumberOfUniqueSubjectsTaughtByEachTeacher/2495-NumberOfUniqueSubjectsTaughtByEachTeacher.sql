-- Last updated: 7/31/2026, 9:32:31 AM
# Write your MySQL query statement below
SELECT 
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;