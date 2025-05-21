WITH Filtered AS (
    SELECT
        id,
        visit_date,
        people,
        ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
Grouped AS (
    SELECT
        id,
        visit_date,
        people,
        id - rn AS grp
    FROM Filtered
),
Counted AS (
    SELECT
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM Grouped
)
SELECT
    id,
    visit_date,
    people
FROM Counted
WHERE cnt >= 3
ORDER BY visit_date;
