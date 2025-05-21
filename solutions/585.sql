SELECT
    ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
JOIN (
    -- policies with a tiv_2015 value appearing more than once
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) dup ON i.tiv_2015 = dup.tiv_2015
JOIN (
    -- policies whose (lat, lon) pair is unique
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
) loc ON i.lat = loc.lat AND i.lon = loc.lon;
