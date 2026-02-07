-- =========================
-- 売上サマリー（全期間）
-- =========================
SELECT
  product_code,
  SUM(sales_qty)    AS total_qty,
  SUM(sales_amount) AS total_amount
FROM sales
GROUP BY product_code
ORDER BY total_amount DESC;

-- =========================
-- KPI（全体）
-- =========================
SELECT
  SUM(sales_amount) AS amount,
  SUM(sales_qty)    AS qty,
  SUM(transactions) AS txns,
  ROUND(CAST(SUM(sales_amount) AS REAL) / NULLIF(SUM(transactions), 0), 0) AS aov,
  ROUND(CAST(SUM(sales_qty) AS REAL) / NULLIF(SUM(transactions), 0), 2) AS upt
FROM sales;

-- =========================
-- 品番 × 性別
-- =========================
SELECT
  product_code,
  gender,
  SUM(sales_amount) AS total_amount
FROM sales
GROUP BY product_code, gender
ORDER BY product_code, total_amount DESC;
