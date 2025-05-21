SELECT
    s.user_id,
    -- If the user has no confirmation records, rate is 0.00
    IFNULL(
      ROUND(c.confirmed_count / c.total_count, 2),
      0.00
    ) AS confirmation_rate
FROM Signups AS s
LEFT JOIN (
    SELECT
        user_id,
        COUNT(*)           AS total_count,
        SUM(action = 'confirmed') AS confirmed_count
    FROM Confirmations
    GROUP BY user_id
) AS c
  ON s.user_id = c.user_id;
