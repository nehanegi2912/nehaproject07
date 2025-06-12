
-- Task 6: Monthly Sales Trend Analysis (MySQL)

SELECT
  DATE_FORMAT(STR_TO_DATE(`Date`, '%d-%m-%Y'), '%Y-%m') AS YearMonth,
  SUM(`Total Revenue`) AS Monthly_Revenue,
  COUNT(DISTINCT `Transaction ID`) AS Order_Volume
FROM `order`
GROUP BY YearMonth
ORDER BY YearMonth;
