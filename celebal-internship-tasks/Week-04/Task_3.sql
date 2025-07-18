-- Weather Observation Station 19
-- https://www.hackerrank.com/challenges/weather-observation-station-19/problem

SELECT ROUND(
    SQRT(
        POW(MAX(LAT_N) - MIN(LAT_N), 2) +
        POW(MAX(LONG_W) - MIN(LONG_W), 2) ), 4 ) 
AS distance
FROM STATION;