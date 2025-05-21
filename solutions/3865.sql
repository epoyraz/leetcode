WITH DistinctPurchases AS (
  SELECT DISTINCT user_id, product_id
  FROM ProductPurchases
)
SELECT
  p1.product_id   AS product1_id,
  p2.product_id   AS product2_id,
  i1.category     AS product1_category,
  i2.category     AS product2_category,
  COUNT(*)        AS customer_count
FROM DistinctPurchases p1
JOIN DistinctPurchases p2
  ON p1.user_id = p2.user_id
 AND p1.product_id < p2.product_id
JOIN ProductInfo i1
  ON p1.product_id = i1.product_id
JOIN ProductInfo i2
  ON p2.product_id = i2.product_id
GROUP BY
  p1.product_id,
  p2.product_id,
  i1.category,
  i2.category
HAVING
  COUNT(*) >= 3
ORDER BY
  customer_count DESC,
  product1_id ASC,
  product2_id ASC;
