CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
DETERMINISTIC
BEGIN
  SET N = N - 1;
  RETURN (
    SELECT salary
    FROM (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT N, 1
    ) AS temp
  );
END;
