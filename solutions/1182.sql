WITH FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
LoggedInAgain AS (
    SELECT DISTINCT a1.player_id
    FROM Activity a1
    JOIN FirstLogin fl
        ON a1.player_id = fl.player_id
    WHERE DATEDIFF(a1.event_date, fl.first_login) = 1
)
SELECT 
    ROUND(COUNT(DISTINCT la.player_id) * 1.0 / COUNT(DISTINCT a.player_id), 2) AS fraction
FROM 
    Activity a
LEFT JOIN 
    LoggedInAgain la
    ON a.player_id = la.player_id;
