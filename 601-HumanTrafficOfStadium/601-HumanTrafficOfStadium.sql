-- Last updated: 7/31/2026, 9:33:56 AM
# Write your MySQL query statement below
WITH filtered AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
grouped AS (
    SELECT *,
           id - rn AS grp
    FROM filtered
),
valid_groups AS (
    SELECT grp
    FROM grouped
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT id, visit_date, people
FROM grouped
WHERE grp IN (SELECT grp FROM valid_groups)
ORDER BY visit_date;