-- 1) Find the user with the most distinct movie ratings (break ties by lexicographically smaller name)
WITH UserRatings AS (
  SELECT
    u.name,
    COUNT(*) AS cnt
  FROM MovieRating mr
  JOIN Users u
    ON mr.user_id = u.user_id
  GROUP BY u.user_id, u.name
),
TopUser AS (
  SELECT name
  FROM UserRatings
  ORDER BY cnt DESC, name ASC
  LIMIT 1
),

-- 2) Find the movie with the highest average rating in February 2020 (break ties by lexicographically smaller title)
FebRatings AS (
  SELECT
    mr.movie_id,
    AVG(mr.rating) AS avg_rating
  FROM MovieRating mr
  WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
  GROUP BY mr.movie_id
),
TopMovie AS (
  SELECT
    m.title
  FROM FebRatings fr
  JOIN Movies m
    ON fr.movie_id = m.movie_id
  ORDER BY fr.avg_rating DESC, m.title ASC
  LIMIT 1
)

-- Combine results into a single column
SELECT name    AS results FROM TopUser
UNION ALL
SELECT title   AS results FROM TopMovie;
