-- Last updated: 7/16/2026, 4:06:06 PM
# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
            WHEN sex = 'm' THEN 'f'
            ELSE 'm'
          END;