WITH RankedSalaries AS (
    SELECT 
        e.id,
        e.name,
        e.salary,
        e.departmentId,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
)
SELECT d.name AS Department, r.name AS Employee, r.salary AS Salary
FROM RankedSalaries r
JOIN Department d ON r.departmentId = d.id
WHERE r.rnk <= 3;
