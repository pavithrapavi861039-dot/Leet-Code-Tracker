-- Last updated: 7/16/2026, 4:09:10 PM
# Write your MySQL query statement below
SELECT 
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;