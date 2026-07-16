-- Last updated: 7/16/2026, 4:08:54 PM
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;