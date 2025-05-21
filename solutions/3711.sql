WITH RECURSIVE
-- 1) Unroll each string into rows (content_id, pos, len, full_text)
positions AS (
  SELECT
    content_id,
    content_text        AS full_text,
    1                    AS pos,
    CHAR_LENGTH(content_text) AS len
  FROM user_content
  UNION ALL
  SELECT
    content_id,
    full_text,
    pos + 1,
    len
  FROM positions
  WHERE pos < len
),
-- 2) Annotate each character with the previous character (or NULL if pos=1)
chars AS (
  SELECT
    content_id,
    pos,
    SUBSTRING(full_text, pos, 1)            AS ch,
    CASE WHEN pos = 1
         THEN NULL
         ELSE SUBSTRING(full_text, pos-1, 1)
    END                                        AS prev
  FROM positions
)
-- 3) Reassemble per content_id, applying our rule:
SELECT
  uc.content_id,
  uc.content_text     AS original_text,
  -- Use GROUP_CONCAT over pos, with empty SEPARATOR, to rebuild in order
  GROUP_CONCAT(
    CASE
      -- If at start or prev is nonâletter, and current is a letter â UPPER
      WHEN (pos = 1 OR prev NOT REGEXP '[A-Za-z]')
           AND ch  REGEXP '[A-Za-z]'
      THEN UPPER(ch)
      -- Otherwise â LOWER
      ELSE LOWER(ch)
    END
    ORDER BY pos
    SEPARATOR ''
  ) AS converted_text
FROM user_content AS uc
JOIN chars USING (content_id)
GROUP BY uc.content_id, uc.content_text
ORDER BY uc.content_id;
