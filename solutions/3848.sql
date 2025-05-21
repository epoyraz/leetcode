SELECT
  ua.user_id,
  -- Average trial duration, rounded to 2 decimals
  ROUND(AVG(CASE WHEN ua.activity_type = 'free_trial'
                 THEN ua.activity_duration
            END), 2) AS trial_avg_duration,
  -- Average paid duration, rounded to 2 decimals
  ROUND(AVG(CASE WHEN ua.activity_type = 'paid'
                 THEN ua.activity_duration
            END), 2) AS paid_avg_duration
FROM UserActivity AS ua
GROUP BY ua.user_id
HAVING 
  -- must have at least one free_trial
  SUM(CASE WHEN ua.activity_type = 'free_trial' THEN 1 ELSE 0 END) > 0
  -- must have at least one paid
  AND SUM(CASE WHEN ua.activity_type = 'paid' THEN 1 ELSE 0 END) > 0
ORDER BY ua.user_id;
