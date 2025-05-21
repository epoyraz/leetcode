WITH boarding AS (
  SELECT
    person_name,
    weight,
    SUM(weight) OVER (ORDER BY turn) AS total_weight,
    turn
  FROM Queue
)
SELECT person_name
FROM boarding
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
