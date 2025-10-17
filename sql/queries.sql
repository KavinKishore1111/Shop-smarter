-- queries.sql

-- Revenue by product category
SELECT Product_Category, SUM(Revenue) AS total_revenue
FROM sales
GROUP BY Product_Category
ORDER BY total_revenue DESC;

-- Top 10 customers by total spend
SELECT Customer_Id, SUM(Revenue) AS total_spent
FROM sales
GROUP BY Customer_Id
ORDER BY total_spent DESC
LIMIT 10;

-- Monthly revenue trend
SELECT DATE_TRUNC('month', Order_Date) AS month, SUM(Revenue) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Underperforming products (lowest revenue)
SELECT Product, SUM(Revenue) AS total_revenue
FROM sales
GROUP BY Product
ORDER BY total_revenue ASC
LIMIT 10;
