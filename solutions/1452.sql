WITH daily AS (
  SELECT
    visited_on,
    SUM(amount) AS daily_amount,
    ROW_NUMBER() OVER (ORDER BY visited_on) AS rn,
    SUM(SUM(amount)) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS window_sum
  FROM Customer
  GROUP BY visited_on
)
SELECT
  visited_on,
  window_sum    AS amount,
  ROUND(window_sum / 7.0, 2) AS average_amount
FROM daily
WHERE rn >= 7
ORDER BY visited_on;
