SELECT
  user_id,
  email
FROM
  Users
WHERE
  email RLIKE '^[[:alnum:]_]+@[[:alpha:]]+\\.com$'
ORDER BY
  user_id;
