-- Weather Observation Station 8
-- https://www.hackerrank.com/challenges/weather-observation-station-8/problem

SELECT CITY FROM STATION 
WHERE LOWER(SUBSTR(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u') 
    AND LOWER(SUBSTR(CITY, -1, 1)) IN ('a', 'e', 'i', 'o', 'u');