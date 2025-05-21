WITH OrderedOps AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY stock_name, operation ORDER BY operation_day) AS rn
    FROM Stocks
),
BuyOps AS (
    SELECT stock_name, operation_day AS buy_day, price AS buy_price, rn
    FROM OrderedOps
    WHERE operation = 'Buy'
),
SellOps AS (
    SELECT stock_name, operation_day AS sell_day, price AS sell_price, rn
    FROM OrderedOps
    WHERE operation = 'Sell'
)
SELECT b.stock_name,
       SUM(s.sell_price - b.buy_price) AS capital_gain_loss
FROM BuyOps b
JOIN SellOps s
  ON b.stock_name = s.stock_name AND b.rn = s.rn
GROUP BY b.stock_name;
