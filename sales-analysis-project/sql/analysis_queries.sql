SELECT * FROM sales_data LIMIT 5;

SELECT 
SUM(Sales) AS Total_Sales, 
SUM(Profit) AS Total_Profit
FROM sales_data;

SELECT Region, Sum(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT Category, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT Year, Month, SUM(Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Year, Month
ORDER BY Year, Month;

SELECT `Customer Name`, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 5;

SELECT `Sub-Category`, SUM(Profit) As Total_Profit
FROM sales_data
GROUP BY `Sub-Category`
HAVING Total_Profit < 0;