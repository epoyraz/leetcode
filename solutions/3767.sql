SELECT
  d.student_id,
  d.subject,
  s_first.score  AS first_score,
  s_last.score   AS latest_score
FROM
  (
    -- find each student/subjectâs earliest and latest exam_date,
    -- and only keep those with at least two different dates
    SELECT
      student_id,
      subject,
      MIN(exam_date) AS first_date,
      MAX(exam_date) AS last_date
    FROM Scores
    GROUP BY student_id, subject
    HAVING MIN(exam_date) < MAX(exam_date)
  ) AS d
  -- join once to get the first examâs score
  JOIN Scores AS s_first
    ON s_first.student_id = d.student_id
   AND s_first.subject    = d.subject
   AND s_first.exam_date  = d.first_date
  -- and again to get the latest examâs score
  JOIN Scores AS s_last
    ON s_last.student_id = d.student_id
   AND s_last.subject    = d.subject
   AND s_last.exam_date  = d.last_date
WHERE
  -- only those whose latest_score > first_score
  s_first.score < s_last.score
ORDER BY
  d.student_id,
  d.subject;
