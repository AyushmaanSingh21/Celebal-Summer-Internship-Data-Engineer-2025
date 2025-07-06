-- Weather Observation Station 20
-- https://www.hackerrank.com/challenges/weather-observation-station-20/problem

SELECT Round(sts.lat_n, 4)
FROM station AS sts
WHERE (SELECT Count(lat_n) FROM station WHERE lat_n < sts.lat_n) = (SELECT Count(lat_n) FROM station WHERE lat_n > sts.lat_n);