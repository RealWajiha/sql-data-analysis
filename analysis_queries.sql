
-- Task 04: Perform SQL Data Analysis
-- Project: Sales Data Analysis System

-- 1. SELECT: Display all customers
SELECT * FROM customers;

-- 2. WHERE: Filter completed orders
SELECT order_id, amount, status
FROM orders
WHERE status = 'Completed';

-- 3. ORDER BY: Sort orders from highest to lowest
SELECT order_id, amount
FROM orders
ORDER BY amount DESC;

-- 4. Aggregate functions: Calculate overall statistics
SELECT
    COUNT(*) AS total_orders,
    SUM(amount) AS total_order_value,
    ROUND(AVG(amount), 2) AS average_order_value,
    MIN(amount) AS minimum_order,
    MAX(amount) AS maximum_order
FROM orders;

-- 5. GROUP BY: Analyze orders by status
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount
FROM orders
GROUP BY status
ORDER BY total_amount DESC;

-- 6. INNER JOIN: Display customer and order details
SELECT
    o.order_id,
    c.name AS customer_name,
    c.city,
    o.amount,
    o.status
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
ORDER BY o.order_id;

-- 7. GROUP BY and JOIN: Calculate spending per customer
SELECT
    c.name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_spent
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;

-- 8. WHERE, GROUP BY and JOIN: Completed sales by city
SELECT
    c.city,
    COUNT(o.order_id) AS completed_orders,
    SUM(o.amount) AS completed_sales
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.city
ORDER BY completed_sales DESC;
