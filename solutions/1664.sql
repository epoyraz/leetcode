# Write your MySQL query statement below
SELECT user_id, name, mail
FROM Users
WHERE 
    -- Must match the domain exactly
    mail LIKE '%@leetcode.com' 
    -- Must start with a letter and allowed characters before the @
    AND mail REGEXP '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$';
