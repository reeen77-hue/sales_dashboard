-- 行数
SELECT COUNT(*) AS n_rows FROM sales;

-- 日付範囲（期間が全部か確認）
SELECT MIN(date) AS min_date, MAX(date) AS max_date
FROM sales;

-- 品番の種類（505がいるか確認）
SELECT DISTINCT product_code
FROM sales
ORDER BY product_code;
