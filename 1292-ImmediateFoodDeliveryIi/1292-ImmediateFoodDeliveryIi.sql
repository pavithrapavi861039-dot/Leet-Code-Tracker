-- Last updated: 7/16/2026, 4:05:02 PM
# Write your MySQL query statement below
SELECT 
    ROUND(
        100 * SUM(order_date = customer_pref_delivery_date) / COUNT(*),
        2
    ) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);