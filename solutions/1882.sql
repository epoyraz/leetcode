SELECT
  e.employee_id,
  e.name,
  COUNT(*) AS reports_count,
  ROUND(AVG(r.age), 0) AS average_age
FROM Employees AS e
JOIN Employees AS r
  ON r.reports_to = e.employee_id
GROUP BY
  e.employee_id,
  e.name
ORDER BY
  e.employee_id;
