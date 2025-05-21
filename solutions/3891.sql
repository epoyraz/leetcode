WITH UserCategories AS (
  -- get each (user, category) only once
  SELECT DISTINCT
    pp.user_id,
    pi.category
  FROM ProductPurchases AS pp
  JOIN ProductInfo       AS pi
    ON pp.product_id = pi.product_id
)

SELECT
  uc1.category      AS category1,
  uc2.category      AS category2,
  COUNT(*)          AS customer_count
FROM UserCategories AS uc1
JOIN UserCategories AS uc2
  ON uc1.user_id = uc2.user_id
  -- only take each unordered pair once:
  AND uc1.category < uc2.category
GROUP BY
  uc1.category,
  uc2.category
HAVING
  customer_count >= 3
ORDER BY
  customer_count DESC,
  category1      ASC,
  category2      ASC;
