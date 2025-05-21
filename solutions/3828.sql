WITH RECURSIVE
levels AS (
  SELECT employee_id, employee_name, manager_id, salary, 1 AS lvl
    FROM Employees
   WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.employee_name, e.manager_id, e.salary, l.lvl+1
    FROM Employees e
    JOIN levels l
      ON e.manager_id = l.employee_id
),
tree AS (
  SELECT employee_id AS ancestor,
         employee_id AS descendant,
         0              AS dist
    FROM Employees
  UNION ALL
  SELECT t.ancestor,
         e.employee_id AS descendant,
         t.dist + 1     AS dist
    FROM tree t
    JOIN Employees e
      ON e.manager_id = t.descendant
)
SELECT
  l.employee_id,
  l.employee_name,
  l.lvl       AS level,
  SUM(CASE WHEN t.dist >= 1 THEN 1 ELSE 0 END) AS team_size,
  -- Fix: don't add l.salary again, just sum all descendant salaries (including self)
  SUM(d.salary) AS budget
FROM levels l
JOIN tree   t ON t.ancestor   = l.employee_id
JOIN Employees d ON d.employee_id = t.descendant
GROUP BY
  l.employee_id,
  l.employee_name,
  l.lvl
ORDER BY
  level        ASC,
  budget       DESC,
  employee_name ASC;
